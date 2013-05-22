from collections import defaultdict
from w3lib.http import basic_auth_header
from scrapy import log, signals

class HubProxyMiddleware(object):

    url = 'http://proxy.crawlera.com:8010'
    maxbans = 20
    ban_code = 503
    download_timeout = 1800

    @classmethod
    def from_crawler(cls, crawler):
        o = cls()
        o.crawler = crawler
        o._bans = defaultdict(int)
        crawler.signals.connect(o.open_spider, signals.spider_opened)
        return o

    def open_spider(self, spider):
        self.enabled = self.is_enabled(spider)
        if not self.enabled:
            return

        for k in ('user', 'pass', 'url', 'maxbans', 'download_timeout'):
            o = getattr(self, k, None)
            s = self.crawler.settings.get('HUBPROXY_' + k.upper(), o)
            v = getattr(spider, 'hubproxy_' + k, s)
            setattr(self, k, v)

        self._proxyauth = self.get_proxyauth(spider)
        log.msg("Using hubproxy at %s (user: %s)" % (self.url, self.user), spider=spider)

    def is_enabled(self, spider):
        """Hook to enable middleware by custom rules"""
        return getattr(spider, 'use_hubproxy', False) \
                or self.crawler.settings.getbool("HUBPROXY_ENABLED")

    def get_proxyauth(self, spider):
        """Hook to compute Proxy-Authorization header by custom rules"""
        return basic_auth_header(self.user, getattr(self, 'pass'))

    def process_request(self, request, spider):
        if self.enabled and 'dont_proxy' not in request.meta:
            request.meta['proxy'] = self.url
            request.meta['download_timeout'] = self.download_timeout
            request.headers['Proxy-Authorization'] = self._proxyauth

    def process_response(self, request, response, spider):
        if self.enabled and response.status == self.ban_code:
            key = request.meta.get('download_slot')
            self._bans[key] += 1
            if self._bans[key] > self.maxbans:
                self.crawler.engine.close_spider(spider, 'banned')
        else:
            key = request.meta.get('download_slot')
            self._bans[key] = 0
        return response

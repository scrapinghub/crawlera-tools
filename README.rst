==============
Crawlera tools
==============

This repository contains tools for the `Crawlera service`_.

crawlera-bench
--------------

``crawlera-bench`` can be used to benchmark Crawlera with your domain. It needs
a file with a list of urls (one per line).

Quick start::

    $ wget https://raw.githubusercontent.com/scrapinghub/crawlera-tools/master/crawlera-bench
    $ chmod a+x crawlera-bench

Usage::

    crawlera-bench urls.txt -u USER -p PASSWORD

For more usage info see::

    crawlera-bench -h

The output would something like this::

    Concurrency     : 100
    Timeout         : 120 sec
    Report interval : 1 sec
    Unit            : requests per 1 sec

    time                netloc                           all   2xx   3xx   4xx   5xx   503   t/o   err  |      minw     maxw
    2014-04-23 17:29:44 www.somesite.com                   0     9     0     0     0     0     0     0  |     0.929   13.958
    2014-04-23 17:29:45 www.somesite.com                   0     4     0     0     0     0     0     0  |     0.846   49.655
    2014-04-23 17:29:46 www.somesite.com                   0    14     0     0     0     0     0     0  |     0.940   50.097
    2014-04-23 17:29:47 www.somesite.com                   0    12     0     0     0     0     0     0  |     0.999   41.884
    2014-04-23 17:29:48 www.somesite.com                   0    17     0     0     0     0     0     0  |     0.932   22.537
    2014-04-23 17:29:49 www.somesite.com                   0    28     0     0     0     0     0     0  |     0.806   15.329
    2014-04-23 17:29:50 www.somesite.com                   0    23     0     0     0     0     0     0  |     0.577    9.809
    2014-04-23 17:29:51 www.somesite.com                   0    33     0     0     0     0     0     0  |     0.602   42.200
    2014-04-23 17:29:52 www.somesite.com                   0    36     0     0     0     0     0     0  |     0.489   46.377
    2014-04-23 17:29:53 www.somesite.com                   0    33     0     0     0     0     0     0  |     0.478   18.375
    2014-04-23 17:29:54 www.somesite.com                   0    42     0     0     0     0     0     0  |     0.430   16.562
    2014-04-23 17:29:55 www.somesite.com                   0    49     0     0     0     0     0     0  |     0.459   36.815
    2014-04-23 17:29:56 www.somesite.com                   0    48     0     0     0     0     0     0  |     0.464   13.926
    2014-04-23 17:29:57 www.somesite.com                   0    40     0     0     0     0     0     0  |     0.610   26.006
    2014-04-23 17:29:58 www.somesite.com                   0    51     0     0     0     0     0     0  |     0.974    6.083
    2014-04-23 17:29:59 www.somesite.com                   0    38     0     0     0     0     0     0  |     0.980   42.102
    2014-04-23 17:30:00 www.somesite.com                   0    54     0     0     0     0     0     0  |     0.663   14.737

Some columns may require an explanation such as:

* ``2xx``, ``3xx``, ... : requests with response code in the 2xx, 3xx, ... range
* ``all``  : all requests combined
* ``t/o``  : requests that timed out
* ``err``  : requests with errors (connection or HTTP errors)
* ``minw`` : minimum request wait time found in the last interval
* ``maxw`` : maximum request wait time found in the last interval

scrapy-crawlera
---------------

A Crawlera middleware for Scrapy. See scrapy-crawlera/README.rst for more details.


.. _Crawlera service: http://crawlera.com/

# -*- coding: utf-8 -*-

# Scrapy settings for lianjia_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lianjia_spider'

SPIDER_MODULES = ['lianjia_spider.spiders']
NEWSPIDER_MODULE = 'lianjia_spider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'lianjia_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 10
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Referer': 'http://hz.fang.lianjia.com/loupan/',
    'Connection': 'keep-alive',
    'Cookie': 'lianjia_uuid=b68981de-415f-4785-aba0-0afb5155ecd0; UM_distinctid=15d97a515da301-0425f52a3c6fc8-8383667-1fa400-15d97a515dbbc0; select_city=330100; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1501487765,1502332753; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1502332753; _smt_uid=597ee294.1a06f9fb; logger_session=e95a64ba08e801fe58526aac69a27b2d; CNZZDATA1256189456=109723742-1501486905-%7C1502356454; _ga=GA1.2.1992599976.1501487767; _gid=GA1.2.706900928.1502332755; CNZZDATA1254525948=1012050688-1501485973-%7C1502356783; CNZZDATA1255633284=837828444-1501484996-%7C1502355751; CNZZDATA1255604082=1437963776-1501486466-%7C1502357346; lianjia_ssid=067d78e3-330d-4d4f-b885-68fccb746b39'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'lianjia_spider.middlewares.LianjiaSpiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'lianjia_spider.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'lianjia_spider.pipelines.LianjiaSpiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# mysql  数据库 连接参数

CONNECT_MYSQL = {
    "host": "192.168.4.238:3306",
    "user": "yong",
    "pwd": "19950105",
    "db": "hsh_fx",
    "charset": "utf8"
}


TABLE_LIST = ['lianjia_loupan', 'lianjia_open_info', 'lianjia_xiangxi_info','lianjia_comment']

# 日志设置
# LOG_ENABLED = False
'''
--- 楼盘信息表
drop TABLE  if EXISTS  `lianjia_loupan`;

CREATE TABLE `lianjia_loupan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `area` varchar(200) DEFAULT NULL,
  `other` varchar(300) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `type` varchar(300) DEFAULT NULL,
  `url` varchar(300) DEFAULT NULL,
  `where` varchar(300) DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  `luopan_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

--- 开盘信息
drop TABLE  if EXISTS  `lianjia_open_info`;

CREATE TABLE `lianjia_open_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `luopan_id` varchar(100) DEFAULT NULL,
  `open_date` varchar(40) DEFAULT NULL,
  `build` varchar(200) DEFAULT NULL,
  `fqbuild` varchar(200) DEFAULT NULL,
  `fqname` varchar(40) DEFAULT NULL,
  `handover_date` varchar(40) DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

--- 详细信息
drop TABLE  if EXISTS  `lianjia_xiangxi_info`;

CREATE TABLE `lianjia_xiangxi_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `luopan_id` varchar(100) DEFAULT NULL,
  `area_ratio` varchar(30) DEFAULT NULL,
  `plan_household` varchar(30) DEFAULT NULL,
  `green_rate` varchar(30) DEFAULT NULL,
  `heating_method` varchar(40) DEFAULT NULL,
  `developer` varchar(100) DEFAULT NULL,
  `parking_spaces` varchar(100) DEFAULT NULL,
  `real_estate` varchar(100) DEFAULT NULL,
  `property_rights` varchar(40) DEFAULT NULL,
  `water_supply` varchar(40) DEFAULT NULL,
  `proposed_price` varchar(40) DEFAULT NULL,
  `build_area` varchar(40) DEFAULT NULL,
  `property_company` varchar(100) DEFAULT NULL,
  `project_charact` varchar(300) DEFAULT NULL,
  `power_supply` varchar(40) DEFAULT NULL,
  `location` varchar(200) DEFAULT NULL,
  `build_type` varchar(40) DEFAULT NULL,
  `regional` varchar(200) DEFAULT NULL,
  `cover_area` varchar(100) DEFAULT NULL,
  `parking_ratio` varchar(100) DEFAULT NULL,
  `property_type` varchar(100) DEFAULT NULL,
  `sales_address` varchar(100) DEFAULT NULL,
  `property_cost` varchar(100) DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;


----------- 评论信息
CREATE TABLE `lianjia_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `luopan_id` varchar(100) DEFAULT NULL,
  `info` varchar(60) DEFAULT NULL,
  `words` varchar(500) DEFAULT NULL,
  `num` varchar(30) DEFAULT NULL,
  `star` varchar(40) DEFAULT NULL,
  `like` varchar(10) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;


'''

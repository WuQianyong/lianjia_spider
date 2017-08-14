#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# 
# Name   : lianjia
# Fatures:
# Author : qianyong
# Time   : 2017/7/31 17:02
# Version: V0.0.1
#

from scrapy.spiders import Spider

from lianjia_spider.items import LianjiaSpiderItem


class LianjiaLoupanSpider(Spider):
    name = 'lianjia'

    start_urls = [
        # 'http://hz.fang.lianjia.com/loupan/pg1nht1/',
        'http://hz.fang.lianjia.com/loupan/pg{}/'.format(i) for i in range(1, 35)
    ]

    host = 'http://hz.fang.lianjia.com'

    def parse(self, response):
        # print(response.text)
        data_area = response.xpath('//*/div[@id="matchid"]/div/div/ul[@id="house-lst"]/li/div[@class="info-panel"]')
        for data_item in data_area:
            item = LianjiaSpiderItem()

            data_info_area = data_item.xpath('div[@class="col-1"]')
            item['name'] = data_info_area[0].xpath('h2/a/text()').extract()[0]
            url_tail = data_info_area[0].xpath('h2/a/@href').extract()[0]
            item['url'] = self.host + url_tail
            item['luopan_id'] = url_tail[8:len(url_tail) - 1]

            item['where'] = data_info_area[0].xpath('div[@class="where"]/span/text()').extract()[0]
            area_list = data_info_area[0].xpath('div[@class="area"]').xpath('string(.)').extract()[0].split('-')
            item['area'] = ' '.join([a.strip() for a in area_list])
            other_list = data_info_area[0].xpath('div[@class="other"]/span/text()').extract()
            item['other'] = ','.join(other_list)
            type_list = data_info_area[0].xpath('div[@class="type"]/span/text()').extract()
            item['type'] = ','.join(type_list)
            price_info_area = data_item.xpath('div[@class="col-2"]/div/div').xpath('string(.)')
            item['price'] = ''.join([a.strip() for a in price_info_area.extract()[0].split('\t')])
            yield item
            # url = response.xpath('//*/div[@class="page-box"]/a')[-1].xpath('@href')
            # print(url)

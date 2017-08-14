#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# 
# Name   : lianjia_info
# Fatures:
# Author : qianyong
# Time   : 2017/8/1 14:27
# Version: V0.0.1
#

"""
链家 开盘信息、规划信息，配套信息，预售许可证
"""

from scrapy.spiders import Spider
from .common import get_urls, INFO_DICT
from lianjia_spider.items import Lianjia_openinfo, Lianjia_infoItem
import logging

class LianjiaInfoSpider(Spider):
    name = 'lianjia_info'

    # start_urls = ['{}xiangqing/'.format(a) for a in get_urls()[:3]]
    start_urls = ['{}xiangqing/'.format(a) for a in get_urls()]

    def parse(self, response):
        logging.info('url:   {}'.format(response.url))
        # === 开盘信息
        if 'redirect' in response.url:
            logging.info('被重定向')
        else:
            open_info_area = response.xpath('//*/ul[@class="fenqi-ul"]')

            # 开盘时间
            open_list = open_info_area[0].xpath('li/span[@class="fq-td fq-open"]/span/text()').extract()
            # 售卖楼栋
            build_list = open_info_area[0].xpath('li/span[@class="fq-td fq-build"]/span/text()').extract()
            # 交房时间
            handover_list = open_info_area[0].xpath('li/span[@class="fq-td fq-handover"]/span/text()').extract()
            # 分期名称
            fqname_list = open_info_area[0].xpath('li/p/span[@class="fq-fqname"]/text()').extract()
            # 分期楼栋
            fqbuild_list = open_info_area[0].xpath('li/p/span[@class="fq-fqbuild"]/span/text()').extract()
            luopan_id = response.url[34:len(response.url) - 11]
            for open_date, build, handover_date, fqname, fqbuild in zip(open_list, build_list, handover_list, fqname_list,
                                                                        fqbuild_list):
                open_item = Lianjia_openinfo()
                open_item['open_date'] = open_date
                open_item['build'] = build
                open_item['handover_date'] = handover_date
                open_item['fqname'] = fqname
                open_item['fqbuild'] = fqbuild
                open_item['luopan_id'] = luopan_id
                yield open_item
            # 规划信息
            plan_info_area = response.xpath('//*/ul[@class="x-box"]/li')
            plan_info_dict = Lianjia_infoItem()
            for x in plan_info_area:
                label = x.xpath('span[@class="label"]/text()').extract()[0].strip()
                label_val = x.xpath('span[contains(@class,"label-val")]').xpath('string(.)').extract()[0].strip()
                if label == '车位：':
                    label_val = ';'.join([a.strip() for a in label_val.split('；')])
                plan_info_dict[INFO_DICT.get(label, 'a')] = label_val
            # print(plan_info_dict)
            plan_info_dict['luopan_id'] = luopan_id
            yield plan_info_dict

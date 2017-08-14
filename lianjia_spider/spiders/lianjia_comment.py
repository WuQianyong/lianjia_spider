#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# 
# Name   : lianjia_comment
# Fatures:
# Author : qianyong
# Time   : 2017/8/10 14:26
# Version: V0.0.1
#
"""
链家的 楼盘评论
"""
from scrapy.spiders import Spider
from scrapy.http import Request, Response, Headers
from .common import get_urls
import math
from lianjia_spider.items import Lianjia_commentItem

class LianjiaCommentSpider(Spider):
    name = 'lianjia_comment'

    def start_requests(self):
        lianjia_url_list = get_urls()
        for comment_url in lianjia_url_list[90:96]:
            # print(self.max_page)
            # print(comment_url)
            url = '{}pinglun/pg{}'.format(comment_url, 1)
            # print(url)
            yield Request(url, callback=self.parse)

            # if i >= self.max_page:
            #     flag = False

    def parse(self, response):
        # print(response.headers)
        try:

            page_num = int(response.url.split('pg')[-1])

            comment_li = response.xpath('//*[@id="user-comment"]/div/div[1]/div[2]/ul[2]/li')
            try:
                max_comment = response.xpath('//*/li[@class="active"]/a/span/text()').extract()[0]
            except:
                max_comment = 0
            max_page = math.ceil(int(max_comment) / 10)

            print(max_page)
            # print(comment_li)
            if max_page != 0:
                if comment_li:
                    luopan_id = response.url.split('/')[-3]
                    for uc1 in comment_li:
                        uc_dict = Lianjia_commentItem()
                        info_list = uc1.xpath('div[@class="l_userpic"]/div[@class="info"]/text()').extract()
                        uc_dict['luopan_id'] = luopan_id
                        uc_dict['info'] = ','.join([x.strip() for x in info_list])
                        uc_dict['star'] = \
                            uc1.xpath('div[@class="r_comment"]/div[@class="score clear"]/div/div/@style').extract()[0]
                        uc_dict['num'] = ','.join(uc1.xpath(
                            'div[@class="r_comment"]/div[@class="score clear"]/div[@class="num"]/span/text()').extract())
                        uc_dict['words'] = uc1.xpath('div[@class="r_comment"]/*/div[@class="words"]/text()').extract()[0]
                        uc_dict['time'] = uc1.xpath('div[@class="r_comment"]/*/div[@class="time"]/text()').extract()[0]
                        uc_dict['like'] = uc1.xpath('div[@class="r_comment"]/*/div[@class="like"]/span/text()').extract()[0]
                        yield uc_dict


                else:
                    print('没有东西')

            if page_num < max_page:
                page_num += 1
                print('---------- {} '.format(page_num))
                url = '{}{}'.format(response.url[:len(response.url) - len(str(page_num))], page_num)
                yield Request(url, callback=self.parse)

        except Exception as e:
            print(e)
            print('出现异常 {} '.format(response.url))
            # print(respon)
            # print

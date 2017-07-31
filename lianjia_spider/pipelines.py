# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from lianjia_spider.items import LianjiaSpiderItem
from lianjia_spider.settings import CONNECT_MYSQL, TABLE_LIST
from plugins.connect_db import _conn
from sqlalchemy import *
import logging
class LianjiaSpiderPipeline(object):
    def process_item(self, item, spider):
        if self.session and self.base:
            day_quotes = self.base.classes[TABLE_LIST[0]]
            if isinstance(item,LianjiaSpiderItem):
                result = self.session.query(day_quotes.id).filter(day_quotes.name == item.get('name'),
                                                                  day_quotes.area == item.get('area'),
                                                                  day_quotes.price == item.get(
                                                                      'price'))
                result_list = list(result)
                if result_list.__len__() == 0:
                    onerecord = day_quotes(name=item.get('name'),
                                           area=item.get('area'),
                                           where=item.get('where'),
                                           other=item.get('other'),
                                           price=item.get('price'),
                                           type=item.get('type'),
                                           url=item.get('url'),
                                           # type=item.get('type'),

                                           # quote_date=quote_date,
                                           updated=func.now())

                    try:
                        self.session.add(onerecord)
                        self.session.commit()
                        logging.info('日行情数据存储成功：{} {} {} {}'.format(item.get('name'),
                                                                    item.get('area'),
                                                                    item.get('where'),
                                                                    item.get('price')))
                    except Exception as e:
                        if 'Duplicate' in str(e):
                            logging.info('日行情存储数据 {} {} {} {} 失败,原因是 数据库已存在该数据 '.format(item.get('name'),
                                                                                        item.get('area'),
                                                                                        item.get(
                                                                                            'where'),
                                                                                        item.get('price')
                                                                                        ))
                        else:
                            logging.error('日行情 存储数据 失败 原因：{}             数据：{}'.format(e, item))
                        self.session.rollback()
        return item

    def open_spider(self, spider):
        try:
            logging.info('打开管道')
            self.session, self.base = _conn(CONNECT_MYSQL, TABLE_LIST)

            logging.info('连接 MySQL  hsh_fx 成功，参数为：{}'.format(CONNECT_MYSQL))
        except Exception as e:
            logging.critical('连接 MySQL 失败')
            self.session, self.base = None, None
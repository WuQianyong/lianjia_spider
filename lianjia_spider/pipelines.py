# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from lianjia_spider.items import LianjiaSpiderItem, Lianjia_openinfo, Lianjia_infoItem
from lianjia_spider.settings import CONNECT_MYSQL, TABLE_LIST
from plugins.connect_db import _conn
from sqlalchemy import *
import logging


class LianjiaSpiderPipeline(object):
    def process_item(self, item, spider):
        if self.session and self.base:
            day_quotes = self.base.classes[TABLE_LIST[0]]
            if isinstance(item, LianjiaSpiderItem):
                result = self.session.query(day_quotes.id).filter(day_quotes.name == item.get('name'),
                                                                  day_quotes.area == item.get('area'),
                                                                  day_quotes.type == item.get('type'),
                                                                  day_quotes.where == item.get('where'),
                                                                  day_quotes.other == item.get('other'),
                                                                  day_quotes.price == item.get('price'))
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
                                           luopan_id=item.get('luopan_id'),
                                           # quote_date=quote_date,
                                           updated=func.now())

                    try:
                        self.session.add(onerecord)
                        self.session.commit()
                        logging.info('链家楼盘 数据存储成功：{} {} {} {}'.format(item.get('name'),
                                                                      item.get('area'),
                                                                      item.get('where'),
                                                                      item.get('price')))
                    except Exception as e:
                        logging.error('链家楼盘 存储数据 失败 原因：{}             数据：{}'.format(e, item))
                        self.session.rollback()
            if isinstance(item, Lianjia_openinfo):
                day_quotes = self.base.classes[TABLE_LIST[1]]
                result = self.session.query(day_quotes.id).filter(day_quotes.luopan_id == item.get('luopan_id'),
                                                                  day_quotes.fqname == item.get('fqname'),
                                                                  day_quotes.open_date == item.get('open_date'),
                                                                  )
                result_list = list(result)
                if result_list.__len__() == 0:
                    onerecord = day_quotes(luopan_id=item.get('luopan_id'),
                                           open_date=item.get('open_date'),
                                           build=item.get('build'),
                                           fqbuild=item.get('fqbuild'),
                                           fqname=item.get('fqname'),
                                           handover_date=item.get('handover_date'),
                                           updated=func.now())
                    try:
                        self.session.add(onerecord)
                        self.session.commit()
                        logging.info('链家开盘 数据存储成功：{} {} {} {}'.format(item.get('luopan_id'),
                                                                      item.get('fqname'),
                                                                      item.get('fqbuild'),
                                                                      item.get('open_date')))
                    except Exception as e:
                        logging.error('链家开盘 存储数据 失败 原因：{}             数据：{}'.format(e, item))
                        self.session.rollback()
            if isinstance(item, Lianjia_infoItem):
                day_quotes = self.base.classes[TABLE_LIST[2]]
                result = self.session.query(day_quotes.id).filter(day_quotes.luopan_id == item.get('luopan_id'))
                result_list = list(result)
                print('======= {}'.format(result_list))
                if result_list.__len__() == 0:
                    onerecord = day_quotes(luopan_id=item.get('luopan_id'),
                                           area_ratio=item.get('area_ratio'),
                                           plan_household=item.get('plan_household'),
                                           green_rate=item.get('green_rate'),
                                           heating_method=item.get('heating_method'),
                                           developer=item.get('developer'),
                                           parking_spaces=item.get('parking_spaces'),
                                           real_estate=item.get('real_estate'),
                                           property_rights=item.get('property_rights'),
                                           water_supply=item.get('water_supply'),
                                           proposed_price=item.get('proposed_price'),
                                           build_area=item.get('build_area'),
                                           property_company=item.get('property_company'),
                                           project_charact=item.get('project_charact'),
                                           power_supply=item.get('power_supply'),
                                           location=item.get('location'),
                                           build_type=item.get('build_type'),
                                           regional=item.get('regional'),
                                           cover_area=item.get('cover_area'),
                                           parking_ratio=item.get('parking_ratio'),
                                           property_type=item.get('property_type'),
                                           sales_address=item.get('sales_address'),
                                           property_cost=item.get('property_cost'),
                                           updated=func.now())
                else:
                    onerecord = day_quotes(id=result_list[0][0],
                                           luopan_id=item.get('luopan_id'),
                                           area_ratio=item.get('area_ratio'),
                                           plan_household=item.get('plan_household'),
                                           green_rate=item.get('green_rate'),
                                           heating_method=item.get('heating_method'),
                                           developer=item.get('developer'),
                                           parking_spaces=item.get('parking_spaces'),
                                           real_estate=item.get('real_estate'),
                                           property_rights=item.get('property_rights'),
                                           water_supply=item.get('water_supply'),
                                           proposed_price=item.get('proposed_price'),
                                           build_area=item.get('build_area'),
                                           property_company=item.get('property_company'),
                                           project_charact=item.get('project_charact'),
                                           power_supply=item.get('power_supply'),
                                           location=item.get('location'),
                                           build_type=item.get('build_type'),
                                           regional=item.get('regional'),
                                           cover_area=item.get('cover_area'),
                                           parking_ratio=item.get('parking_ratio'),
                                           property_type=item.get('property_type'),
                                           sales_address=item.get('sales_address'),
                                           property_cost=item.get('property_cost'),
                                           updated=func.now())

                try:
                    self.session.add(onerecord)
                    self.session.commit()
                    logging.info('链家详细 数据存储成功：{} {} {} {}'.format(item.get('luopan_id'),
                                                                  item.get('plan_household'),
                                                                  item.get('build_area'),
                                                                  item.get('project_charact')))
                except Exception as e:
                    logging.error('链家详细 存储数据 失败 原因：{}             数据：{}'.format(e, item))
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

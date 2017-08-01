#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# 
# Name   : common
# Fatures:
# Author : qianyong
# Time   : 2017/8/1 14:39
# Version: V0.0.1
#

from plugins.connect_db import _conn
from lianjia_spider.settings import CONNECT_MYSQL, TABLE_LIST


def get_urls():
    session, base = _conn(CONNECT_MYSQL, TABLE_LIST)
    # print(TABLE_LIST)
    luopan = base.classes[TABLE_LIST[0]]
    result = session.query(luopan.url)
    # print(list(result))
    print(len(list(result)))
    result_list = list(set([a[0] for a in list(result)]))
    print(len(result_list))
    return result_list


INFO_DICT = {
    '容积率：': 'area_ratio',
    '规划户数：': 'plan_household',
    '绿化率：': 'green_rate',
    '供暖方式：': 'heating_method',
    '开发商：': 'developer',
    '车位：': 'parking_spaces',
    '楼盘户型：': 'real_estate',
    '产权年限：': 'property_rights',
    '供水方式：': 'water_supply',
    '参考价格：': 'proposed_price',
    '建筑面积：': 'build_area',
    '物业公司：': 'property_company',
    '项目特色：': 'project_charact',
    '供电方式：': 'power_supply',
    '楼盘地址：': 'location',
    '建筑类型：': 'build_type',
    '区域位置：': 'regional',
    '占地面积：': 'cover_area',
    '车位配比：': 'parking_ratio',
    '物业类型：': 'property_type',
    '售楼处地址：': 'sales_address',
    '物业费：': 'property_cost',

}

if __name__ == '__main__':
    print(get_urls())

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
from scrapy import Field, Item


class LianjiaSpiderItem(Item):
    # define the fields for your item here like:
    name = Field()
    url = Field()
    where = Field()
    area = Field()
    other = Field()
    type = Field()
    price = Field()
    luopan_id = Field()

    # pass


class Lianjia_openinfo(Item):
    luopan_id = Field()
    open_date = Field()
    build = Field()
    handover_date = Field()
    fqname = Field()
    fqbuild = Field()

class Lianjia_commentItem(Item):
    luopan_id = Field()
    info = Field()
    words = Field()
    num = Field()
    time = Field()
    star = Field()
    like = Field()

class Lianjia_infoItem(Item):
    luopan_id=Field()
    area_ratio = Field()
    plan_household = Field()
    green_rate = Field()
    heating_method = Field()
    developer = Field()
    real_estate = Field()
    parking_spaces = Field()
    property_rights = Field()
    water_supply = Field()
    proposed_price = Field()
    build_area = Field()
    property_company = Field()
    cover_area = Field()
    project_charact = Field()
    power_supply = Field()
    location = Field()
    build_type = Field()
    regional = Field()
    parking_ratio = Field()
    sales_address = Field()
    property_cost = Field()
    property_type = Field()



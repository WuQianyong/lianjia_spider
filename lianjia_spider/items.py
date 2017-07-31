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

    # pass

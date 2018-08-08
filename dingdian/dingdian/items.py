# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DingdianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #小说名字
    name = scrapy.Field()
    #作者
    author = scrapy.Field()
    #小说地址
    novelurl = scrapy.Field()
    #状态
    serialstatus = scrapy.Field()
    #连载字数
    serialnumber = scrapy.Field()
    #文章类别
    category = scrapy.Field()
    #小说编号
    name_id = scrapy.Field()


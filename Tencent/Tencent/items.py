# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
     # 职位名称
     positionName = scrapy.Field()
     # 公司组织
     organization=scrapy.Field()
     # 职位地址
     positionLocation = scrapy.Field()
     # 职位类型
     positionType = scrapy.Field()
     # 发布时间
     releaseTime = scrapy.Field()
     # 职位链接
     # positionLink = scrapy.Field()
     # 职位简介
     positionBrief = scrapy.Field()

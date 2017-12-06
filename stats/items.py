# -*- coding: utf-8 -*-
import scrapy


class AreaItem(scrapy.Item):
    name = scrapy.Field()
    href = scrapy.Field()
    area_id = scrapy.Field()
    parent_id = scrapy.Field()
    pass

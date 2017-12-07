# -*- coding: utf-8 -*-
import scrapy


class AreaItem(scrapy.Item):
    name = scrapy.Field()
    level = scrapy.Field()
    href = scrapy.Field()
    area_id = scrapy.Field()
    parent_id = scrapy.Field()
    pass


class Area5Item(scrapy.Item):
    name = scrapy.Field()
    level = scrapy.Field()
    href = scrapy.Field()
    area_id = scrapy.Field()
    parent_id = scrapy.Field()
    category_code = scrapy.Field()
    pass
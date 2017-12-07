# -*- coding: utf-8 -*-
import scrapy
from ..items import AreaItem
import os


class Area1Spider(scrapy.Spider):
    name = 'area1'
    allowed_domains = ['http://www.stats.gov.cn']
    start_urls = ['http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/index.html']
    base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/'

    def parse(self, response):
        print("正在解释省份" + "." * 200)
        item = AreaItem()
        name_list = response.xpath(".//tr[@class='provincetr']/td/a/text()").extract()
        href_list = response.xpath(".//tr[@class='provincetr']/td/a/@href").extract()
        for name, href in zip(name_list, href_list):
            item["area_id"] = os.path.splitext(href)[0]
            item["name"] = name
            item["level"] = 1
            item["href"] = self.base_url + href
            item["parent_id"] = 0
            yield item
        pass

# -*- coding: utf-8 -*-
import scrapy
from ..items import AreaItem
import os
import pymysql


class Area2Spider(scrapy.Spider):
    name = "area2"
    base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/'

    def start_requests(self):
        urls = []
        db = pymysql.connect("127.0.0.1", "root", "123456", "stats", charset="utf8")
        cur = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select href from 2016_area where parent_id=0"
        cur.execute(sql)
        href_list = cur.fetchall()
        for one in href_list:
            yield scrapy.Request(one["href"])

    def parse(self, response):
        item = AreaItem()
        area_id_list = response.xpath(".//tr[@class='citytr']/td[1]/a/text()").extract()
        name_list    = response.xpath(".//tr[@class='citytr']/td[2]/a/text()").extract()
        href_list    = response.xpath(".//tr[@class='citytr']/td[2]/a/@href").extract()
        for area_id, name, href in zip(area_id_list, name_list, href_list):
            item["area_id"] = area_id
            item["name"] = name
            item["href"] = self.base_url + href
            item["parent_id"] = os.path.dirname(href)
            yield item
        pass

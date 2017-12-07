# -*- coding: utf-8 -*-
import scrapy
from ..items import Area5Item
import os
import pymysql


class Area2Spider(scrapy.Spider):
    name = "area5"

    def start_requests(self):
        db = pymysql.connect("127.0.0.1", "root", "123456", "stats", charset="utf8")
        cur = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select href from 2016_area where level=4 "
        cur.execute(sql)
        href_list = cur.fetchall()
        for one in href_list:
            yield scrapy.Request(one["href"])

    def parse(self, response):
        item = Area5Item()
        node_list = response.xpath(".//table[@class='villagetable']")
        one_area = node_list.xpath("./tr[@class='villagetr']")
        for node in one_area:
            area_id = node.xpath("./td[1]/text()").extract()[0]
            item["area_id"] = area_id
            item["name"] = node.xpath("./td[3]/text()").extract()[0]
            item["category_code"] = node.xpath("./td[2]/text()").extract()[0]
            item["level"] = 5
            item["href"] = ""
            item["parent_id"] = area_id[0:9] + '000'
            yield item
        pass

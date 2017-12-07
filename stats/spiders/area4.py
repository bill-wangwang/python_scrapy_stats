# -*- coding: utf-8 -*-
import scrapy
from ..items import AreaItem
import os
import pymysql


class Area2Spider(scrapy.Spider):
    name = "area4"

    def start_requests(self):
        urls = []
        db = pymysql.connect("127.0.0.1", "root", "123456", "stats", charset="utf8")
        cur = db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select href from 2016_area where level=3 and href != '' "
        cur.execute(sql)
        href_list = cur.fetchall()
        for one in href_list:
            yield scrapy.Request(one["href"])

    def parse(self, response):
        item = AreaItem()
        base_url = os.path.dirname(response.url) + "/"
        node_list = response.xpath(".//table[@class='towntable']")
        one_area = node_list.xpath("./tr[@class='towntr']")
        for node in one_area:
            try:
                area_id = node.xpath("./td[1]/a/text()").extract()[0]
            except:
                area_id = None
            if area_id is None:
                area_id = node.xpath("./td[1]/text()").extract()[0]
                href = ""
                name = node.xpath("./td[2]/text()").extract()[0]
            else:
                href = base_url + node.xpath("./td[2]/a/@href").extract()[0]
                name = node.xpath("./td[2]/a/text()").extract()[0]
            item["area_id"] = area_id
            item["name"] = name
            item["level"] = 4
            item["href"] = href
            item["parent_id"] = area_id[0:6] + '000000'
            yield item
        pass

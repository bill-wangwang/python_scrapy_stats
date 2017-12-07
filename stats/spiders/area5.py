# -*- coding: utf-8 -*-
import scrapy
from ..items import Area5Item
import os
import pymysql


class Area2Spider(scrapy.Spider):
    name = "area5"
    # start_urls = ["http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/21/11/04/211104006.html",
    #               "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/22/24/01/222401101.html",
    #               "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/23/11/21/231121106.html",
    #               "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/33/07/82/330782106.html",
    #               "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/33/07/84/330784001.html",
    #               "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/35/06/81/350681501.html",
    #               "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/36/09/82/360982200.html",
    #               "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/45/09/21/450921112.html",
    #               "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/45/09/21/450921113.html",
    #               "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/52/26/33/522633108.html",
    #               "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/52/27/22/522722105.html",
    #               "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/52/27/28/522728114.html",
    #               "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/53/07/22/530722107.html",
    #               "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/53/09/22/530922204.html",
    #               "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/61/05/27/610527102.html",
    #               "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/61/07/25/610725117.html",
    #               "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/62/05/25/620525102.html",
    #               "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/62/08/26/620826210.html",
    #               "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/62/08/26/620826216.html",
    #               "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/64/05/22/640522213.html",
    #               "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/65/31/30/653130103.html"]

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

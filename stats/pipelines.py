# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class AreaPipeline(object):

    def __init__(self):
        self.db = None
        self.cur = None

    def open_spider(self, spider):
        self.db = pymysql.connect("127.0.0.1", "root", "123456", "stats", charset="utf8")
        self.cur = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    def process_item(self, item, spider):
        # `area_id`, `parent_id`, `name`, `href`
        insert_sql = "insert into 2016_area (`area_id`, `parent_id`, `name`, `href`) values({}, {},'{}', '{}')" . \
            format(item['area_id'], item['parent_id'],  item['name'], item['href'])
        print(insert_sql)
        self.cur.execute(insert_sql)
        self.db.commit()
        return item

    def spider_close(self, spider):
        self.db.close()

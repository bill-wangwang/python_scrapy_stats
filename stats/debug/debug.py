# -*- coding: utf-8 -*-
import pymysql

urls = []
db = pymysql.connect("127.0.0.1", "root", "123456", "stats", charset="utf8")
cur = db.cursor(cursor=pymysql.cursors.DictCursor)
sql = "select href from 2016_area where parent_id=0"
cur.execute(sql)
href_list = cur.fetchall()
for one in href_list:
    urls.append(one["href"])
print(urls)

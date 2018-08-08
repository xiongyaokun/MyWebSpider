# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import mysql.connector
from . import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

class DingdianPipeline(object):

    def __init__(self):
        self.conn = mysql.connector.connect(
            host=MYSQL_HOSTS,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWORD,
            db=MYSQL_DB,
            charset='utf8',
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            sql = "INSERT INTO dd_name(xs_name, xs_author, category, name_id) VALUES (%s,%s,%s,%s)"
            # self.cursor.execute(sql, ('xiong','lili', '123', 'yaokun'))
            self.cursor.execute(sql, (item['name'], item['author'], item['category'], item['name_id']))
            self.conn.commit()
        except Exception as e:
            print(e)
        return item

    def close_spider(self, spider):
        self.conn.close()

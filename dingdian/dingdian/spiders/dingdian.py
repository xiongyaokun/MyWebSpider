# -*- coding: utf-8 -*-

import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from dingdian.items import DingdianItem

# import sys
# import random

# reload(sys)
# sys.setdefaultencoding('utf-8')

class Myspider(scrapy.Spider):
    
    name = 'dingdian'
    allowed_domains = ['23us.so']
    base_url = 'http://www.23us.so/list/'
    baseurl = '.html'

    def start_requests(self):
        for i in range(1, 10):
            url = self.base_url + str(i) + '_1' + self.baseurl
            yield Request(url, self.parse)
        yield Request('http://www.23us.so/full.html', self.parse)

    def parse(self, response):
        # print(response.text)
        max_num = BeautifulSoup(response.text, 'lxml').find('div', class_='pagelink').find_all('a')[-1].get_text()
        baseurl = str(response.url)[:-7]
        for num in range(1, int(max_num) + 1):
            url = baseurl + '_' + str(num) + self.baseurl
            yield Request(url, callback=self.get_name)

    def get_name(self, response):
        tds = BeautifulSoup(response.text, 'lxml').find_all('tr', bgcolor='#FFFFFF')
        for td in tds:
            novelname = td.find('a').get_text()
            novelurl = td.find('a')['href']
            yield Request(novelurl, callback=self.get_chapterurl, meta={'name': novelname, 'url': novelurl})

    def get_chapterurl(self, response):
        item = DingdianItem()
        item['name'] = ((response.meta['name']).replace('\xa0', ''))
        item['novelurl'] = response.meta['url'].encode('utf-8')
        category = BeautifulSoup(response.text, 'lxml').find('table').find('a').get_text()
        author = BeautifulSoup(response.text, 'lxml').find('table').find_all('td')[1].get_text()
        base_url = BeautifulSoup(response.text, 'lxml').find('p', class_='btnlinks').find('a', class_='read')['href']
        # name_id = ((base_url)[-11:-5].replace('/', '')).encode('utf-8')
        pattern = re.compile(r'\d+')
        # name_id = pattern.findall(str(base_url))[1].encode('utf-8')
        name_id = pattern.findall(str(response.meta['url']))[1]

        item['category'] = ((category).replace('/', ''))
        item['author'] = (str(author).replace('\xa0', ''))
        item['name_id'] = name_id

        # return item
        yield item


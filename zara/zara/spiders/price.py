# -*- coding: utf-8 -*-
import scrapy
from zara.items import ZaraMenPrice


class ZaramenshirtSpider(scrapy.Spider):
    name = 'zaramenshirt'
    allowed_domains = ['www.zara.com/in/en/man-shirts-l737.html?v1=1181080']
    start_urls = ['https://www.zara.com/in/en/man-shirts-l737.html?v1=1181080/']

    def parse(self, response):
        items = ZaraMenPrice()
        price = response.xpath('//div[@price _product-price"]/span/@data-price')
        # for href in response.xpath('//div[@price _product-price"]/span/@data-price'):
        items['price'] = ''.join(price).strip() if price else None
        yield items

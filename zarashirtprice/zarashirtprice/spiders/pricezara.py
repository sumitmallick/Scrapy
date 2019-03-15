# -*- coding: utf-8 -*-
import scrapy
from zarashirtprice.items import ZarashirtpriceItem


class PricezaraSpider(scrapy.Spider):
    name = 'pricezara'
    allowed_domains = ['https://www.zara.com/in/en/man-shirts-l737.html?v1=1181080']
    start_urls = ['http://https://www.zara.com/in/en/man-shirts-l737.html?v1=1181080/']

    def parse(self, response):
        price = response.xpath('//div[@price _product-price"]/span/@data-price')
        # for href in response.xpath('//div[@price _product-price"]/span/@data-price'):
        items['price'] = ''.join(price).strip() if price else None
        yield items
        


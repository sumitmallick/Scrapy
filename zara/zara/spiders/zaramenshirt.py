# -*- coding: utf-8 -*-
import scrapy
from zara.items import ZaraData


class ZaramenshirtPriceSpider(scrapy.Spider):
    name = 'zaramenprice'
    allowed_domains = ['www.zara.com/in/en/man-shirts-l737.html?v1=1181080']
    start_urls = ['https://www.zara.com/in/en/man-shirts-l737.html?v1=1181080/']

    def parse(self, response):
        items = ZaraData()
        
        for href in response.xpath('//ul[@class="submenuUtilities"]/li/a/@href'):
        	items['url'] = response.urljoin(href.extract())
        	yield items

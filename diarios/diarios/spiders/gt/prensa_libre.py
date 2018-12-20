# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

from diarios.items import DiariosItem


class PrensaLibreGTSpider(scrapy.Spider):
    name = 'plgt'
    allowed_domains = ['https://www.prensalibre.com/opinion']
    start_urls = ['https://www.prensalibre.com/opinion']
    custom_settings = {
        'ROBOTSTXT_OBEY': True,
    }


    def parse(self, response):
        """
        @url http://www.prensalibre.com/
        @returns items 1 14
        @returns requests 0 0
        @scrapes author title url
        """
        autores_staff = response.css(".name")
        
        for selector in selectors:
            yield self.parse_article(selector, response)

    def parse_article(self, selector, response):
        loader = ItemLoader(DiariosItem(), selector=selector)

        loader.add_xpath('title', './/h2//text()')
        loader.add_xpath('author', './/a[@class="nombre"]/text()')
        loader.add_xpath('url', './/h2//@href')
        return loader.load_item()


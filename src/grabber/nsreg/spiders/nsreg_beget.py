# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent, EMPTY_PRICE, find_price
from ..items import NsregItem


class NsregWebnamesSpider(scrapy.Spider):
    name = 'nsreg_beget'
    allowed_domains = ['beget.com']
    start_urls = ['https://beget.com/ru/domains/zone/ru']
    site_names = ("ООО «Бегет»",)

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex={
                'price_reg': r'([0-9]{3})',
                'price_prolong': r'([0-9]{3})',
                'price_change': r'.*?(\d+)\s*рублей.*',
            },
            path={
                'price_reg': '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/p[2]/text()',
                'price_prolong': '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[2]/p[2]/text()',
                'price_change': '/html/body/div[1]/div/div/div[3]/div[1]/div/div/div/div[3]/div[2]/div/div[1]/ul[3]/li[1]/text()',
            },
        )

    def parse_price_change(self, response):
        price_change = response.xpath(self.component.path['price_change']).get()
        price_change = find_price(self.component.regex['price_change'], price_change)
        item = NsregItem()
        item['name'] = self.site_names[0]
        price = item.get('price', EMPTY_PRICE)
        price['price_change'] = price_change
        item['price'] = price

        yield item

    def parse(self, response):
        price_reg = response.xpath(self.component.path['price_reg']).get()
        price_reg = find_price(self.component.regex['price_reg'], price_reg)

        price_prolong = response.xpath(self.component.path['price_prolong']).get()
        price_prolong = find_price(self.component.regex['price_prolong'], price_prolong)

        yield scrapy.Request(
            'https://beget.com/ru/kb/how-to/domains/kak-perenesti-domeny-v-beget',
            callback=self.parse_price_change,
        )

        item = NsregItem()
        item['name'] = self.site_names[0]
        price = item.get('price', EMPTY_PRICE)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        item['price'] = price

        return item

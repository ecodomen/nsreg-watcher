# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent, EMPTY_PRICE, find_price
from ..items import NsregItem


class NsregWebnamesSpider(scrapy.Spider):
    name = "nsreg_nic"
    allowed_domains = ["www.nic.ru"]
    start_urls = ["https://www.nic.ru/catalog/domains/ru/"]
    site_names = ("АО «РСИЦ»",)

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex={
                'price_reg': r'(\d+)\sруб\.',
                'price_prolong': r'(\d+)\sруб\./год\*',
                'price_change': r'(\d+)\sруб\.',
            },
            path={
                'price_reg': '/html/body/div[1]/div/div/section/div[2]/div/div/p[4]/strong/text()',
                'price_prolong': '/html/body/div[1]/div/div/div[1]/main/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/span/text()',
                'price_change': '/html/body/div[1]/div/div/section/div[2]/div/div/p[6]/strong/text()',
            },
        )

    def parse_price_prolong(self, response):
        price_prolong = response.xpath(self.component.path['price_prolong']).get()
        price_prolong = find_price(self.component.regex['price_prolong'], price_prolong)
        item = NsregItem()
        item['name'] = self.site_names[0]
        price = item.get('price', EMPTY_PRICE)
        price['price_prolong'] = price_prolong
        item['price'] = price

        yield item

    def parse(self, response):
        price_reg = response.xpath(self.component.path['price_reg']).get()
        price_reg = find_price(self.component.regex['price_reg'], price_reg)

        yield scrapy.Request(
            'https://www.nic.ru/catalog/domain-renewal-prices/',
            callback=self.parse_price_prolong,
        )

        price_change = response.xpath(self.component.path['price_change']).get()
        price_change = find_price(self.component.regex['price_change'], price_change)

        item = NsregItem()
        item['name'] = self.site_names[0]
        price = item.get('price', EMPTY_PRICE)
        price['price_reg'] = price_reg
        price['price_change'] = price_change
        item['price'] = price

        return item

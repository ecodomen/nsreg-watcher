# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent, EMPTY_PRICE, find_price
from ..items import NsregItem


class NsregWebnamesSpider(scrapy.Spider):
    name = 'nsreg_2domains'
    allowed_domains = ['2domains.ru']
    start_urls = ['https://2domains.ru/domains']
    site_names = ("ООО «2ДОМЕЙНС.РУ»",)

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex={
                'price_reg': r'(\d+)\s*₽',
                'price_prolong': r'\s*Продление\s*—\s*(\d+)\s*₽\s*',
                'price_change': r'(\d+)\s*₽',
            },
            path={
                'price_reg': '/html/body/div/div[1]/section[3]/div/div[1]/div[1]/a/div[2]/text()',
                'price_prolong': '/html/body/div/div[1]/section[3]/div/div[1]/div[1]/a/div[4]/text()',
                'price_change': '//*[@id="tab00"]/div/div[1]/div[1]/span/text()',
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
            'https://2domains.ru/domains/transfer',
            callback=self.parse_price_change,
        )

        item = NsregItem()
        item['name'] = self.site_names[0]
        price = item.get('price', EMPTY_PRICE)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        item['price'] = price

        return item

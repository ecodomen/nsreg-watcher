# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent, EMPTY_PRICE, find_price
from ..items import NsregItem


class NsregWebnamesSpider(scrapy.Spider):
    name = "nsreg_domainsnethouse"
    allowed_domains = ["domains.nethouse.ru"]
    start_urls = ["https://domains.nethouse.ru/domains"]
    site_names = ("ООО «Регистрант»",)

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex={
                'price_reg': r'([0-9]{3})',
                'price_prolong': r'продление\n\s*от\s*(\d+)\n\s*₽\/год\s*',
                'price_change': r'([0-9]{3})',
            },
            path={
                'price_reg': '/html/body/main/div[2]/form/section/div/div[1]/div[2]/div/div[1]/text()',
                'price_prolong': '/html/body/main/div[2]/form/section/div/div[1]/div[2]/div/div[2]/text()',
                'price_change': '/html/body/main/section[6]/div/div/ul/li[2]/div[2]/p[2]/span/text()',
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
            'https://domains.nethouse.ru/',
            callback=self.parse_price_change,
        )

        item = NsregItem()
        item['name'] = self.site_names[0]
        price = item.get('price', EMPTY_PRICE)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        item['price'] = price

        return item

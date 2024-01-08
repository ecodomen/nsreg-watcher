# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent, EMPTY_PRICE, find_price
from ..items import NsregItem


class NsregWebnamesSpider(scrapy.Spider):
    name = "nsreg_domenus"
    allowed_domains = ["domenus.ru"]
    start_urls = ["https://www.domenus.ru/domain/zone/ru"]
    site_names = ("ООО «Регистратор»",)

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r'([0-9]{3})',
            path={
                'price_reg': '/html/body/main/div[1]/div[3]/div/div/div[2]/div[2]/span/text()',
                'price_prolong': '/html/body/main/div[1]/div[3]/div/div/div[1]/div[2]/text()',
                'price_change': '/html/body/main/div[1]/div/div/p[3]/strong/text()',
            },
        )

    def parse_price_change(self, response):
        price_change = response.xpath(self.component.path['price_change']).get()
        price_change = find_price(self.component.regex['price_change'], price_change)
        item = NsregItem()
        item['name'] = "ООО «Регистратор»"
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
            'https://www.domenus.ru/support/help/group/1343472/question/perenos-domenov-ru-su-rf-k-registratoru-domenus-ru-ot-drugogo-registratora',
            callback=self.parse_price_change,
        )

        item = NsregItem()
        item['name'] = "ООО «Регистратор»"
        price = item.get('price', EMPTY_PRICE)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        item['price'] = price

        return item

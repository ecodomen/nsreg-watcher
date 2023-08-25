# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import find_price, PRICE_DEFAULT_DICT
from ..items import NsregItem


class Nsreg2domainsSpider(scrapy.Spider):
    name = 'nsreg_2domains'
    allowed_domains = ('2domains.ru', )
    start_urls = ('https://2domains.ru/domains', )
    site_name = 'ООО «2ДОМЕЙНС.РУ»'

    page_price_change = "https://2domains.ru/domains/transfer"

    def parse(self, response):
        price_reg = response.xpath('/html/body/div/div[1]/section[3]/div/div[1]/div[1]/a/div[2]/text()').get()
        price_reg = find_price(r"([0-9]+)", price_reg)

        price_prolong = response.xpath('/html/body/div/div[1]/section[3]/div/div[1]/div[1]/a/div[4]/text()').get()
        price_prolong = find_price(r"Продление — ([0-9]+)", price_prolong)

        # Переходим на другую страницу для сбора информации
        yield scrapy.Request(url=self.page_price_change, callback=self.parse_change,
                             cb_kwargs={"price_reg": price_reg,
                                        "price_prolong": price_prolong})

    def parse_change(self, response, price_reg, price_prolong):
        price_change = response.xpath('//*[@id="tab00"]/div/div[1]/div[1]/span/text()').get()
        price_change = find_price(r"([0-9]+)", price_change)

        # Создаем Item для сайта
        item = NsregItem()
        item['name'] = self.site_name
        price = item.get('price', PRICE_DEFAULT_DICT)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        price['price_change'] = price_change
        item['price'] = price

        # Возвращаем готовый Item
        return item

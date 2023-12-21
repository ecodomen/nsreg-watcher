# -*- coding: utf-8 -*-
import scrapy
from nsreg.items import NsregItem

from ..utils import find_price, find_price_withoutre

REGEX_PATTERN = r"([0-9]+)[.,\s]?₽.*"
EMPTY_PRICE = {
    'price_reg': None,
    'price_prolong': None,
    'price_change': None,
}

class NsregWebnamesSpider(scrapy.Spider):
    name = 'nsreg_webnames'
    allowed_domains = ['webnames.ru']
    start_urls = ['https://www.webnames.ru/tld/catalog/ru']

    def parse_price_change(self, response):
        price_change = response.xpath(
            '/html/body/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/span/text()').get()
        price_change = find_price_withoutre(price_change)

        item = NsregItem()
        item['name'] = "ООО «Регтайм»"
        price = item.get('price', EMPTY_PRICE)
        price['price_change'] = price_change
        item['price'] = price

        yield item

    def parse(self, response):
        price_reg = response.xpath(
            '/html/body/section[1]/div[4]/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/strong/text()').get()
        price_reg = find_price(REGEX_PATTERN, price_reg)

        price_prolong = response.xpath(
            '/html/body/section[1]/div[4]/div[1]/div[2]/div/table/tbody/tr[3]/td[2]/strong/text()').get()
        price_prolong = find_price(REGEX_PATTERN, price_prolong)

        yield scrapy.Request('https://www.webnames.ru/domains/transfer', callback=self.parse_price_change)

        item = NsregItem()
        item['name'] = "ООО «Регтайм»"
        price = item.get('price', EMPTY_PRICE)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        item['price'] = price

        yield item
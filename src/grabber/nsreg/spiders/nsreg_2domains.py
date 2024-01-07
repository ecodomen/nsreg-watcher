# -*- coding: utf-8 -*-
import scrapy
from nsreg.items import NsregItem

from ..utils import find_price, find_price_withoutre

# работает

REGEX_PROLONG_PATTERN = r".*Продление\s+—\s+(([0-9]*[.,])?[0-9]+)\s+₽.*"
REGEX_CHANGE_PATTERN = r".*(([0-9]*[.,])?[0-9]{3})\s+₽.*"
EMPTY_PRICE = {
    'price_reg': None,
    'price_prolong': None,
    'price_change': None,
}


class Nsreg2domainsSpider(scrapy.Spider):
    name = 'nsreg_2domains'
    allowed_domains = ['2domains.ru']
    start_urls = ['https://2domains.ru/domains']

    def parse_price_change(self, response):
        price_change = response.xpath('/html/body/div/div[1]/section[1]/div/div/div/div/div[2]/div[2]/div/span/text()').get()
        price_change = find_price(REGEX_CHANGE_PATTERN, price_change)

        item = NsregItem()
        item['name'] = "ООО «2ДОМЕЙНС.РУ»"
        price = item.get('price', EMPTY_PRICE)
        price['price_change'] = price_change
        item['price'] = price

        yield item

    def parse(self, response):
        price_reg = response.xpath('//*[@id="app"]/div[1]/section[3]/div/div[1]/div[1]/a/div[2]/text()').get()
        price_reg = find_price_withoutre(price_reg)

        price_prolong = response.xpath('//*[@id="app"]/div[1]/section[3]/div/div[1]/div[1]/a/div[4]/text()').get()
        price_prolong = find_price(REGEX_PROLONG_PATTERN, price_prolong)

        item = NsregItem()
        item['name'] = "ООО «2ДОМЕЙНС.РУ»"
        price = item.get('price', EMPTY_PRICE)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        item['price'] = price

        yield scrapy.Request('https://2domains.ru/domains/transfer', callback=self.parse_price_change)

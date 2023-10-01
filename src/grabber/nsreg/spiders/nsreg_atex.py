# -*- coding: utf-8 -*-
import scrapy
from nsreg.items import NsregItem

from ..utils import find_price
# работает

REGEX_PATTERN = r".*(([0-9]*[.,])?[0-9]{3}).*"
EMPTY_PRICE = {
    'price_reg': None,
    'price_prolong': None,
    'price_change': None,
}


class NsregAtexSpider(scrapy.Spider):
    name = 'nsreg_atex'
    allowed_domains = ['atex.ru']
    start_urls = ['https://atex.ru/domains/']

    def parse(self, response):
        price_reg = response.xpath(
            '/html/body/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr[1]/td[2]/div/text()').get()
        price_reg = find_price(REGEX_PATTERN, price_reg)

        price_prolong = response.xpath(
            '/html/body/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr[3]/td[2]/div/text()').get()
        price_prolong = find_price(REGEX_PATTERN, price_prolong)

        price_change = response.xpath(
            '/html/body/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr[5]/td[2]/div/text()').get()
        price_change = find_price(REGEX_PATTERN, price_change)

        item = NsregItem()
        item['name'] = "ООО «Атекс»"
        price = item.get('price', EMPTY_PRICE)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        price['price_change'] = price_change
        item['price'] = price

        yield item

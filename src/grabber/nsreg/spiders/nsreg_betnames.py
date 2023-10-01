# -*- coding: utf-8 -*-
import scrapy
from nsreg.items import NsregItem

from ..utils import find_price_sub


REGEX_PATTERN = r".*(\d+\s+\d+).*"
EMPTY_PRICE = {
    'price_reg': None,
    'price_prolong': None,
    'price_change': None,
}


class NsregBetnamesSpider(scrapy.Spider):
    name = "nsreg_betnames"
    allowed_domains = ["betnames.ru"]
    start_urls = ["https://betnames.ru/#features-2"]

    def parse(self, response):
        price_reg = response.xpath(
            '//*[@id="features-2"]/div/div/div[1]/div/p/text()').get()
        price_reg = find_price_sub(REGEX_PATTERN, price_reg)

        price_prolong = response.xpath(
            '//*[@id="features-2"]/div/div/div[2]/div/p/text()').get()
        price_prolong = find_price_sub(REGEX_PATTERN, price_prolong)

        price_change = response.xpath(
            '//*[@id="features-2"]/div/div/div[3]/div/p/text()').get()
        price_change = find_price_sub(REGEX_PATTERN, price_change)

        item = NsregItem()
        item['name'] = "ООО «Бэтнеймс»"
        price = item.get('price', EMPTY_PRICE)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        price['price_change'] = price_change
        item['price'] = price

        yield item

# -*- coding: utf-8 -*-
import scrapy
from nsreg.items import NsregItem

from ..utils import find_price
# работает
REGEX_PATTERN = r"([0-9]+[.,\s])?руб[.]"
EMPTY_PRICE = {
    'price_reg': None,
    'price_prolong': None,
    'price_change': None,
}


class NsregNicSpider(scrapy.Spider):
    name = "nsreg_nic"
    allowed_domains = ["www.nic.ru"]
    start_urls = ["https://www.nic.ru/catalog/domains/ru/"]

    def parse(self, response):
        price_reg = response.xpath(
            '/html/body/div[1]/div/div/section/div[2]/div/div/p[4]/strong/text()').get()
        price_reg = find_price(REGEX_PATTERN, price_reg)

        price_prolong = None

        price_change = response.xpath(
            '/html/body/div[1]/div/div/section/div[2]/div/div/p[6]/strong/text()').get()
        price_change = find_price(REGEX_PATTERN, price_change)

        item = NsregItem()
        item['name'] = "АО «РСИЦ»"
        price = item.get('price', EMPTY_PRICE)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        price['price_change'] = price_change
        item['price'] = price

        yield item

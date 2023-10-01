# -*- coding: utf-8 -*-
import scrapy
from nsreg.items import NsregItem

from ..utils import find_price
# работает
REGEX_PATTERN = r"([0-9]+)[.,\s]?руб.*"
EMPTY_PRICE = {
    'price_reg': None,
    'price_prolong': None,
    'price_change': None,
}


class NsregKlondikeSpider(scrapy.Spider):
    name = "nsreg_klondike"
    allowed_domains = ["klondike-studio.ru"]
    start_urls = ["https://klondike-studio.ru/domain/prices/"]

    def parse(self, response):
        price_reg = response.xpath(
            '/html/body/div[2]/section/div/div/table/tbody/tr[1]/td[2]/text()').get()
        price_reg = find_price(REGEX_PATTERN, price_reg)

        price_prolong = response.xpath(
            '/html/body/div[2]/section/div/div/table/tbody/tr[3]/td[2]/text()').get()
        price_prolong = find_price(REGEX_PATTERN, price_prolong)

        price_change = response.xpath(
            '/html/body/div[2]/section/div/div/table/tbody/tr[5]/td[2]/text()').get()
        price_change = find_price(REGEX_PATTERN, price_change)

        item = NsregItem()
        item['name'] = "ООО «Клондайк Групп»"
        price = item.get('price', EMPTY_PRICE)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        price['price_change'] = price_change
        item['price'] = price

        yield item

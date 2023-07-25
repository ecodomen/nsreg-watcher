# -*- coding: utf-8 -*-
import scrapy
from nsreg.items import NsregItem

from ..utils import find_price
# работает
REGEX_PATTERN = r"([0-9]+)[.,\s]?руб.*"
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}


class NsregKlondikeSpider(scrapy.Spider):
    name = "nsreg_klondike"
    allowed_domains = ["klondike-studio.ru"]
    start_urls = ["https://klondike-studio.ru/domain/prices/"]

    def parse(self, response):
        pricereg = response.xpath(
            '/html/body/div[2]/section/div/div/table/tbody/tr[1]/td[2]/text()').get()
        pricereg = find_price(REGEX_PATTERN, pricereg)

        priceprolong = response.xpath(
            '/html/body/div[2]/section/div/div/table/tbody/tr[3]/td[2]/text()').get()
        priceprolong = find_price(REGEX_PATTERN, priceprolong)

        pricechange = response.xpath(
            '/html/body/div[2]/section/div/div/table/tbody/tr[5]/td[2]/text()').get()
        pricechange = find_price(REGEX_PATTERN, pricechange)

        item = NsregItem()
        item['name'] = "ООО «Клондайк Групп»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange
        item['price'] = price

        yield item

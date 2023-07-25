# -*- coding: utf-8 -*-
import scrapy
from nsreg.items import NsregItem

from ..utils import find_price
# работает
REGEX_PATTERN = r"([0-9]+[.,\s])?руб[.]"
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}


class NsregNicSpider(scrapy.Spider):
    name = "nsreg_nic"
    allowed_domains = ["www.nic.ru"]
    start_urls = ["https://www.nic.ru/catalog/domains/ru/"]

    def parse(self, response):
        pricereg = response.xpath(
            '/html/body/div[1]/div/div/section/div[2]/div/div/p[4]/strong/text()').get()
        pricereg = find_price(REGEX_PATTERN, pricereg)

        priceprolong = None

        pricechange = response.xpath(
            '/html/body/div[1]/div/div/section/div[2]/div/div/p[6]/strong/text()').get()
        pricechange = find_price(REGEX_PATTERN, pricechange)

        item = NsregItem()
        item['name'] = "АО «РСИЦ»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange
        item['price'] = price

        yield item

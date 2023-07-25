# -*- coding: utf-8 -*-
import scrapy
from nsreg.items import NsregItem

from ..utils import find_price
# работает, нет переноса, только с консультацией

REGEX_PATTERN = r"([0-9]{3,}).*"
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}


class NsregBegetSpider(scrapy.Spider):
    name = 'nsreg_beget'
    allowed_domains = ['beget.com']
    start_urls = ['https://beget.com/ru/domains/zone/ru']

    def parse(self, response):
        pricereg = response.xpath(
            '//*[@id="__layout"]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/p[2]/text()').get()
        pricereg = find_price(REGEX_PATTERN, pricereg)

        priceprolong = response.xpath(
            '//*[@id="__layout"]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[2]/p[2]/text()').get()
        priceprolong = find_price(REGEX_PATTERN, priceprolong)

        item = NsregItem()
        item['name'] = "ООО «Бегет»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        item['price'] = price

        yield item

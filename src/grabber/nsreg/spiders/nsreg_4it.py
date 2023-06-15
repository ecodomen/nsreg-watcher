# -*- coding: utf-8 -*-
import logging
import re

import scrapy
from nsreg.items import NsregItem

from ..utils import find_price
#работает
REGEX_PATTERN = r"(([0-9]*[.,])?[0-9]*)\s+₽.*"
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}
class Nsreg4itSpider(scrapy.Spider):
    name = "nsreg_4it"
    allowed_domains = ["4it.ru"]
    start_urls = ["https://4it.ru/#price"]

    def parse(self, response):
        pricereg = response.xpath('/html/body/div[1]/div[4]/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]/div/table/tbody/tr[2]/td[2]/div/p/text()').get()
        pricereg = find_price(REGEX_PATTERN, pricereg)
        
        priceprolong = response.xpath('/html/body/div[1]/div[4]/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tr[2]/td/div/p/text()').get()
        priceprolong = find_price(REGEX_PATTERN, priceprolong)

        pricechange = response.xpath('/html/body/div[1]/div[4]/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div[3]/table/tr[2]/td/div/p/text()').get()
        pricechange = find_price(REGEX_PATTERN, pricechange)

        item = NsregItem()
        item['name'] = "ООО «ИТ»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange 
        item['price'] = price

        yield item

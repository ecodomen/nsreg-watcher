# -*- coding: utf-8 -*-
import logging
import re

import scrapy
from nsreg.items import NsregItem

from ..utils import find_price
#работает
REGEX_PATTERN = r".*(([0-9]*[.,])?[0-9]{3})\s+₽.*"
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}


class NsregDomainySpider(scrapy.Spider):
    name = "nsreg_domeny"
    allowed_domains = ["domeny.ru"]
    start_urls = ["https://domeny.ru/"]

    def parse(self, response):
        pricereg = response.xpath('/html/body/div[2]/div[1]/div[5]/div/div/div/div[3]/a[1]/h5/text()').get()
        pricereg = find_price(REGEX_PATTERN, pricereg)

        item = NsregItem()
        item['name'] = "ООО «Доменный Мастер»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        item['price'] = price

        yield item
        
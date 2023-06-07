# -*- coding: utf-8 -*-
import logging
import re

import scrapy
from nsreg.items import NsregItem

from ..utils import find_price
#работает
REGEX_PATTERN = r"([0-9]+[.,\s])?руб"
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}


class NsregBestregSpider(scrapy.Spider):
    name = "nsreg_bestreg"
    allowed_domains = ["www.bestreg24.ru"]
    start_urls = ["https://www.bestreg24.ru/price/"]

    def parse(self, response):
        pricereg = response.xpath('/html/body/div[1]/div[3]/article/section/table[1]/tr/td[1]/article[1]/div/table/tr[5]/td[2]/text()').get()
        pricereg = find_price(REGEX_PATTERN, pricereg)
        
        priceprolong = response.xpath('/html/body/div[1]/div[3]/article/section/table[1]/tr/td[1]/article[1]/div/table/tr[5]/td[3]/text()').get()
        priceprolong = find_price(REGEX_PATTERN, priceprolong)

        pricechange = response.xpath('/html/body/div[1]/div[3]/article/section/table[2]/tr/td[1]/article[2]/div/table/tr[10]/td[2]/text()').get()
        pricechange = find_price(REGEX_PATTERN, pricechange)

        item = NsregItem()
        item['name'] = "ООО «БЕСТРЕГ»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange 
        item['price'] = price

        yield item

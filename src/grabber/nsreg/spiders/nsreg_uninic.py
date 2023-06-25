# -*- coding: utf-8 -*-
import logging
import re

import scrapy
from nsreg.items import NsregItem

from ..utils import find_price_withoutre
#работает
REGEX_PATTERN = r"([0-9]+[.,\s])?руб"
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}


class NsregUninicSpider(scrapy.Spider):
    name = 'nsreg_uninic'
    allowed_domains = ['uninic.ru']
    start_urls = ['https://uninic.ru/domainreg.php']

    def parse(self, response):
        pricereg = response.xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[3]/table/tr[2]/td[3]/b[1]/text()').get()
        pricereg = find_price_withoutre(pricereg)
        
        priceprolong = response.xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[3]/table/tr[2]/td[5]/b[1]/text()').get()
        priceprolong = find_price_withoutre(priceprolong)

        pricechange = None

        item = NsregItem()
        item['name'] = "ООО «Объединенные доменные имена»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange 
        item['price'] = price

        yield item
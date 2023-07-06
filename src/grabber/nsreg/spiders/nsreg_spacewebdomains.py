# -*- coding: utf-8 -*-
import logging
import re

import scrapy
from nsreg.items import NsregItem

from ..utils import find_price, find_price_withoutre
#работает

REGEX_PROLONG_PATTERN = r".*Продление\s+—\s+(([0-9]*[.,])?[0-9]+)\s+₽.*"
REGEX_CHANGE_PATTERN = r".*(([0-9]*[.,])?[0-9]{3})\s+₽.*"
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}

class Nsreg2domainsSpider(scrapy.Spider):
    name = 'nsreg_spacewebdomains'
    allowed_domains = ['spacewebdomains.ru']
    start_urls = ['https://spacewebdomains.ru/%D1%82%D0%B0%D1%80%D0%B8%D1%84%D1%8B/']

    def parse(self, response):
        pricereg = response.xpath('/html/body/div[1]/div/div[1]/main/article/div/div/figure/table/tbody/tr[2]/td[2]/text()').get().replace(' ', '')
        pricereg = find_price_withoutre(pricereg)

        priceprolong = response.xpath('/html/body/div[1]/div/div[1]/main/article/div/div/figure/table/tbody/tr[3]/td[2]/text()').get().replace(' ', '')
        priceprolong = find_price(REGEX_PROLONG_PATTERN, priceprolong)

        pricechange = response.xpath('/html/body/div[1]/div/div[1]/main/article/div/div/figure/table/tbody/tr[4]/td[2]/text()').get().replace(' ', '')
        pricechange = find_price(REGEX_CHANGE_PATTERN, pricechange)

        item = NsregItem()
        item['name'] = "ООО «СпейсВэб»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange 
        item['price'] = price

        yield item

       
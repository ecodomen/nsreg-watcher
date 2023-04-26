# -*- coding: utf-8 -*-
import logging
import re

import scrapy
from nsreg.items import NsregItem

from spiders.utils import *
#работает

REGEX_PATTERN = r".*(([0-9]*[.,])?[0-9]{3}).*"
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}


class NsregAtexSpider(scrapy.Spider):
    name = 'nsreg_atex'
    allowed_domains = ['atex.ru']
    start_urls = ['https://atex.ru/domains/']

    def parse(self, response):
        pricereg = response.xpath('/html/body/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr[1]/td[2]/div/text()').get()
        pricereg = find_price(REGEX_PATTERN, pricereg)
        
        priceprolong = response.xpath('/html/body/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr[3]/td[2]/div/text()').get()
        priceprolong = find_price(REGEX_PATTERN, priceprolong)

        pricechange = response.xpath('/html/body/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr[5]/td[2]/div/text()').get()
        pricechange = find_price(REGEX_PATTERN, pricechange)


        item = NsregItem()
        item['name'] = "ООО «Атекс»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange 
        item['price'] = price

        yield item

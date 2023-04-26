# -*- coding: utf-8 -*-
import logging
import re

import scrapy
from nsreg.items import NsregItem

from spiders.utils import *
#работает

REGEX_PATTERN = r".*([0-9]+[\s][0-9]{3}).*"
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}

class NsregAltnamesSpider(scrapy.Spider):
    name = 'nsreg_altnames'
    allowed_domains = ['altnames.ru']
    start_urls = ['http://altnames.ru/']

    def parse(self, response):
        pricereg = response.xpath('//*[@id="post-10"]/div/div/div/div/section[4]/div/div/div/div[2]/div/table/tbody/tr[1]/td[2]/text()').get()
        pricereg = find_price_sub(REGEX_PATTERN, pricereg)
        
        priceprolong = response.xpath('//*[@id="post-10"]/div/div/div/div/section[4]/div/div/div/div[2]/div/table/tbody/tr[2]/td[2]/text()').get()
        priceprolong = find_price_sub(REGEX_PATTERN, priceprolong)

        pricechange = response.xpath('//*[@id="post-10"]/div/div/div/div/section[4]/div/div/div/div[2]/div/table/tbody/tr[3]/td[2]/text()').get()
        pricechange = find_price_sub(REGEX_PATTERN, pricechange)

        item = NsregItem()
        item['name'] = "ООО «АЛЬТЕРНАТИВА»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange 
        item['price'] = price

        yield item

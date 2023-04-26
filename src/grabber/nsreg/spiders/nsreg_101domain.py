# -*- coding: utf-8 -*-
import logging
import re

import scrapy
from nsreg.items import NsregItem

from spiders.utils import *
#работает
REGEX_PATTERN = r"([0-9]+[.,\s])?руб"
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}


class Nsreg101domainSpider(scrapy.Spider):
    name = 'nsreg_101domain'
    allowed_domains = ['sidename.ru']
    start_urls = ['https://sidename.ru/site/tariffs']
    

    def parse(self, response):
        pricereg = response.xpath('/html/body/section/div/div/div/div[2]/div[1]/div[2]/span/text()').get()
        pricereg = find_price(REGEX_PATTERN, pricereg)
        
        priceprolong = response.xpath('/html/body/section/div/div/div/div[2]/div[2]/div[2]/span/text()').get()
        priceprolong = find_price(REGEX_PATTERN, priceprolong)

        pricechange = response.xpath('/html/body/section/div/div/div/div[2]/div[3]/div[2]/span/text()').get()
        pricechange = find_price(REGEX_PATTERN, pricechange)

        item = NsregItem()
        item['name'] = "ООО «101домен Регистрация Доменов»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange 
        item['price'] = price

        yield item

    
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


class NsregBeelineSpider(scrapy.Spider):
    name = 'nsreg_beeline'
    allowed_domains = ['moskva.beeline.ru']
    start_urls = ['https://moskva.beeline.ru/business/domen/registratsiya-i-podderzhka-domenov/']

    def parse(self, response):
        pricereg = response.xpath('//*[@id="react_aDGOLumF5U2Eyvb2G5m2g"]/div/div[3]/div[3]/section[1]/div/section/div[2]/div[2]/div[1]/div/div[2]/div[1]/span/text()').get()
        pricereg = find_price(REGEX_PATTERN, pricereg)
        
        priceprolong = response.xpath('//*[@id="react_aDGOLumF5U2Eyvb2G5m2g"]/div/div[3]/div[3]/section[1]/div/section/div[2]/div[2]/div[1]/div/div[2]/div[1]/span/text()').get()
        priceprolong = find_price(REGEX_PATTERN, priceprolong)

        pricechange = None

        item = NsregItem()
        item['name'] = "ПАО «ВымпелКом»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange 
        item['price'] = price

        yield item

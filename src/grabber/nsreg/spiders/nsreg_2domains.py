# -*- coding: utf-8 -*-
import logging
import re

import scrapy
from nsreg.items import NsregItem

REGEX_PROLONG_PATTERN = r".*Продление\s+—\s+(([0-9]*[.,])?[0-9]+)\s+₽.*"
REGEX_CHANGE_PATTERN = r".*(([0-9]*[.,])?[0-9]{3})\s+₽.*"
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}

class Nsreg2domainsSpider(scrapy.Spider):
    name = 'nsreg_2domains'
    allowed_domains = ['2domains.ru']
    start_urls = ['https://2domains.ru/domains']

    def parse_pricechange(self, response):
        pricechange = response.xpath('/html/body/div/div[1]/section[1]/div/div/div/div/div[2]/div[2]/div/span/text()').get()
        pricechange = str(pricechange).strip()
        if m := re.match(REGEX_CHANGE_PATTERN, pricechange):
            pricechange = m.group(1)
            pricechange = f'{float(pricechange)}'
            logging.info('pricechange = %s', pricechange)
        item = NsregItem()
        item['name'] = "ООО «2ДОМЕЙНС.РУ»"  
        price = item.get('price', EMPTY_PRICE)
        price['pricechange'] = pricechange 
        item['price'] = price  

        yield item  

    def parse(self, response):
        pricereg = response.xpath('//*[@id="app"]/div[1]/section[3]/div/div[1]/div[1]/a/div[2]/text()').get()
        pricereg = f"{float(pricereg)}"

        priceprolong = response.xpath('//*[@id="app"]/div[1]/section[3]/div/div[1]/div[1]/a/div[4]/text()').get()
        priceprolong = str(priceprolong)
        priceprolong = priceprolong.strip()
        if m := re.match(REGEX_PROLONG_PATTERN, priceprolong, re.MULTILINE):
            priceprolong = m.group(1)
            priceprolong = f'{float(priceprolong)}'
            logging.info('priceprolong = %s', priceprolong)
    
        yield scrapy.Request('https://2domains.ru/domains/transfer', callback=self.parse_pricechange)

        item = NsregItem()
        item['name'] = "ООО «2ДОМЕЙНС.РУ»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        item['price'] = price

        yield item

       
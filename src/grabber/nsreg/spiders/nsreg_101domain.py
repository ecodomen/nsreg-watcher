# -*- coding: utf-8 -*-
import logging
import re

import scrapy
from nsreg.items import NsregItem

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
        pricereg = str(pricereg).strip()
        if m := re.match(REGEX_PATTERN,pricereg):
            pricereg = m.group(1)
            pricereg = f'{float(pricereg)}'
            logging.info('pricereg = %s', pricereg)
        
        priceprolong = response.xpath('/html/body/section/div/div/div/div[2]/div[2]/div[2]/span/text()').get()
        priceprolong = str(priceprolong).strip()
        if m := re.match(REGEX_PATTERN, priceprolong):
            priceprolong = m.group(1)
            priceprolong = f'{float(priceprolong)}'
            logging.info('priceprolong = %s', priceprolong)

        pricechange = response.xpath('/html/body/section/div/div/div/div[2]/div[3]/div[2]/span/text()').get()
        pricechange = str(pricechange).strip()
        if m := re.match(REGEX_PATTERN, pricechange):
            pricechange = m.group(1)
            pricechange = f'{float(pricechange)}'
            logging.info('pricechange = %s', pricechange)

        item = NsregItem()
        item['name'] = "ООО «101домен Регистрация Доменов»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange 
        item['price'] = price

        yield item

    
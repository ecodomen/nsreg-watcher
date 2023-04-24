# -*- coding: utf-8 -*-
import logging
import re

import scrapy
from nsreg.items import NsregItem

#не работает xpath

REGEX_PATTERN = r".*(([0-9]*[.,])?[0-9]{3}).*"
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
        pricereg = response.xpath('//*[@id="post-10"]/div/div/div/div/section[4]/div/div/div/div[2]/div/table/tbody[2]/tr[1]/td[2]/text()').get()
        pricereg = str(pricereg).strip()
        if m := re.match(REGEX_PATTERN, pricereg):
            pricereg = m.group(1)
            pricereg = f'{float(pricereg)}'
            logging.info('pricereg = %s', pricereg)
        
        priceprolong = response.xpath('//*[@id="post-10"]/div/div/div/div/section[4]/div/div/div/div[2]/div/table/tbody[2]/tr[2]/td[2]/text()').get()
        priceprolong = str(priceprolong).strip()
        if m := re.match(REGEX_PATTERN, priceprolong):
            priceprolong = m.group(1)
            priceprolong = f'{float(priceprolong)}'
            logging.info('priceprolong = %s', priceprolong)

        pricechange = response.xpath('//*[@id="post-10"]/div/div/div/div/section[4]/div/div/div/div[2]/div/table/tbody[2]/tr[3]/td[2]/text()').get()
        pricechange = str(pricechange).strip()
        if m := re.match(REGEX_PATTERN, pricechange):
            pricechange = m.group(1)
            pricechange = f'{float(pricechange)}'
            logging.info('pricechange = %s', pricechange)

        item = NsregItem()
        item['name'] = "ООО «АЛЬТЕРНАТИВА»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange 
        item['price'] = price

        yield item

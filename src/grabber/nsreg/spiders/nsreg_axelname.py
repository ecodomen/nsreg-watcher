# -*- coding: utf-8 -*-
import logging
import re

import scrapy
from nsreg.items import NsregItem

#перенос по диагностике
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}


class NsregAxelnameSpider(scrapy.Spider):
    name = 'nsreg_axelname'
    allowed_domains = ['axelname.ru']
    start_urls = ['https://axelname.ru/domains/']

    def parse(self, response):
        pricereg = response.xpath('//*[@id="pricing-tables1-h"]/div/div/div[1]/div[1]/div/span[2]/text()').get()
        pricereg = str(pricereg).strip()
        pricereg = f'{float(pricereg)}'
        logging.info('pricereg = %s', pricereg)
        
        priceprolong = response.xpath('//*[@id="pricing-tables1-h"]/div/div/div[1]/div[1]/div/span[2]/text()').get()
        priceprolong = str(priceprolong).strip()
        priceprolong = f'{float(priceprolong)}'
        logging.info('priceprolong = %s', priceprolong)
        item = NsregItem()
        item['name'] = "ООО «АксельНейм»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        item['price'] = price

        yield item

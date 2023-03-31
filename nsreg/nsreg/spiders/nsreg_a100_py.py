# -*- coding: utf-8 -*-
import logging
import re

import scrapy
from nsreg.items import NsregItem

REGEX_PATTERN = r"([0-9]*[.,\s])?[0-9]+\s*₽"

class Nsreg2domainsSpider(scrapy.Spider):
    name = 'nsreg_a100'
    allowed_domains = ['a100.ru']
    start_urls = ['https://a100.ru/']

    def parse(self, response):
        pricereg = response.xpath('//*[@id="overlappable"]/div/div/div/div[1]/div/div/div[2]/div/p[1]/text()').get()
        if m := re.match(REGEX_PATTERN, str(pricereg)):
            pricereg = f'{float(pricereg)}'
            logging.info('pricereg = %s', pricereg)
        
        priceprolong = response.xpath('//*[@id="overlappable"]/div/div/div/div[2]/div/div/div[2]/div/p[1]/text()').get()
        if m := re.match(REGEX_PATTERN, str(priceprolong)):
            priceprolong = f'{float(priceprolong)}'
            logging.info('priceprolong = %s', priceprolong)
        item = NsregItem()
        item['name'] = "ООО «А100»"
        item['note1'] = ''
        item['note2'] = ''
        item['city'] = ''
        item['website'] = ''
        item['price'] = {
            'pricereg': pricereg,
            'priceprolong': priceprolong,
        }

        yield item

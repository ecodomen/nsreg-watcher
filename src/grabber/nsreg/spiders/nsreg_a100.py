# -*- coding: utf-8 -*-
import logging
import re

import scrapy
from nsreg.items import NsregItem

REGEX_PATTERN = r".*(\d+\s+\d+).*"

class Nsreg_ad100Spider(scrapy.Spider):
    name = 'nsreg_a100'
    allowed_domains = ['a100.ru']
    start_urls = ['file:///home/rezvov_vadim/projects/nsreg-watcher/docs/A100.RU — Регистрация доменов.html']
        # start_urls = ['https://a100.ru/']


    def parse(self, response):
        pricereg = response.xpath('//*[@id="overlappable"]/div/div/div/div[1]/div/div/div[2]/div/p[1]/text()').get()
        pricereg = str(pricereg)
        if m := re.match(REGEX_PATTERN, pricereg):
            pricereg = m.group(1)
            pricereg = re.sub(r'\s', '', pricereg)
            pricereg = f'{float(pricereg)}'
            logging.info('pricereg = %s', pricereg)
        
        priceprolong = response.xpath('//*[@id="overlappable"]/div/div/div/div[2]/div/div/div[2]/div/p[1]/text()').get()
        priceprolong = str(priceprolong)
        if m := re.match(REGEX_PATTERN, priceprolong):
            priceprolong = m.group(1)
            priceprolong = re.sub(r'\s', '', priceprolong)
            priceprolong = f'{float(priceprolong)}'
            logging.info('priceprolong = %s', priceprolong)

        pricechange = response.xpath('//*[@id="overlappable"]/div/div/div/div[3]/div/div/div[2]/div/p[1]/text()').get()
        pricechange = str(pricechange)
        if m := re.match(REGEX_PATTERN, pricechange):
            pricechange = m.group(1)
            pricechange = re.sub(r'\s', '', pricechange)
            pricechange = f'{float(pricechange)}'
            logging.info('pricechange = %s', pricechange)

        item = NsregItem()
        item['name'] = "ООО «А100»"
        item['note1'] = ''
        item['note2'] = ''
        item['city'] = ''
        item['website'] = ''
        item['price'] = {
            'pricereg': pricereg,
            'priceprolong': priceprolong,
            'pricechange': pricechange,
        }

        yield item

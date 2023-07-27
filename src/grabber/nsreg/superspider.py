# -*- coding: utf-8 -*-
import scrapy
from nsreg.items import NsregItem
import logging
import re

EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
    }

class SuperSpider(scrapy.Spider):
    rusname : str
    pathreg: str
    pathchange: str
    pathprolong: str
    regex_reg: str
    regex_change: str
    regex_prolong: str

    

    def parse(self, response):
        pricereg = response.xpath(self.pathreg).get()
        pricereg = self.find_price(self.regex_reg, pricereg)

        priceprolong = response.xpath(self.pathprolong).get()
        priceprolong = self.find_price(self.regex_prolong, priceprolong)

        pricechange = response.xpath(self.pathchange).get()
        pricechange = self.find_price(self.regex_change, pricechange)

        item = NsregItem()
        item['name'] = self.rusname
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange
        item['price'] = price

        yield item

    def find_price(self, re_pattern, price):
        price = str(price).strip()
        print('!!!!!!!!!!!', price)
        if price == "бесплатно":
            price = 0
        elif re_pattern == '':
            price = re.sub(r'\s', '', price)
        else:
            if m := re.match(re_pattern, price):
                price = m.group(1)
        print('&!&!&!&!&!&!&!&!&', price)
        price = f'{float(price)}'
        logging.info('price = %s', price)

        return price



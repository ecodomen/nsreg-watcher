import logging
import re

import scrapy
from nsreg.items import NsregItem

REGEX_PATTERN = r"([0-9]+[.,\s])?руб"

class Nsreg2domainsSpider(scrapy.Spider):
    name = 'nsreg_101domain'
    allowed_domains = ['sidename.ru']
    start_urls = ['https://sidename.ru/site/tariffs']

    def parse(self, response):
        pricereg = response.xpath('/html/body/section/div/div/div/div[2]/div[1]/div[2]/span/text()').get()
        if m := re.match(REGEX_PATTERN, str(pricereg)):
            pricereg = f'{float(pricereg)}'
            logging.info('pricereg = %s', pricereg)
        
        priceprolong = response.xpath('/html/body/section/div/div/div/div[2]/div[2]/div[2]/span/text()').get()
        if m := re.match(REGEX_PATTERN, str(priceprolong)):
            priceprolong = f'{float(priceprolong)}'
            logging.info('priceprolong = %s', priceprolong)
        item = NsregItem()
        item['name'] = "ООО «101домен Регистрация Доменов»"
        item['note1'] = ''
        item['note2'] = ''
        item['city'] = ''
        item['website'] = ''
        item['price'] = {
            'pricereg': pricereg,
            'priceprolong': priceprolong,
        }

        yield item

import logging
import re

import scrapy
from nsreg.items import NsregItem

REGEX_PATTERN = r".*([0-9]+\.).*"


class Nsreg2domainsSpider(scrapy.Spider):
    name = 'nsreg_aab'
    allowed_domains = ['aab.ru']
    start_urls = ['https://aab.ru/tarifi_na_uslugi.html']

    def parse(self, response):
        pricereg = response.xpath('//*[@id="full_story"]/table/tbody/tr[3]/td[2]/text()').get()
        if m := re.match(REGEX_PATTERN, str(pricereg)):
            pricereg = f'{float(pricereg)}'
            logging.info('pricereg = %s', pricereg)
        
        priceprolong = response.xpath('//*[@id="full_story"]/table/tbody/tr[6]/td[2]/text()').get()
        if m := re.match(REGEX_PATTERN, str(priceprolong)):
            priceprolong = f'{float(priceprolong)}'
            logging.info('priceprolong = %s', priceprolong)
        item = NsregItem()
        item['name'] = "ООО «ААБ Медиа»"
        item['note1'] = ''
        item['note2'] = ''
        item['city'] = ''
        item['website'] = ''
        item['price'] = {
            'pricereg': pricereg,
            'priceprolong': priceprolong,
        }

        yield item

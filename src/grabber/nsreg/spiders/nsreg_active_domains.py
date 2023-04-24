# -*- coding: utf-8 -*-
import logging
import re

import scrapy
from nsreg.items import NsregItem

#работает

REGEX_PATTERN = r".*(([0-9]*[.,])?[0-9]{3}).*"
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}

class NsregActiveDomainsSpider(scrapy.Spider):
    name = 'nsreg_active_domains'
    allowed_domains = ['active.domains']
    start_urls = ['http://active.domains/domains/']

    def parse(self, response):
        pricereg = response.xpath('//*[@id="show_domain"]/div/div/table/tbody/tr[1]/td[3]/a/text()').get()
        pricereg = str(pricereg).strip()
        if m := re.match(REGEX_PATTERN, pricereg):
            pricereg = m.group(1)
            pricereg = f'{float(pricereg)}'
            logging.info('pricereg = %s', pricereg)
        
        priceprolong = response.xpath('//*[@id="show_domain"]/div/div/table/tbody/tr[1]/td[4]/a/text()').get()
        priceprolong = str(priceprolong).strip()
        if m := re.match(REGEX_PATTERN, priceprolong):
            priceprolong = m.group(1)
            priceprolong = f'{float(priceprolong)}'
            logging.info('priceprolong = %s', priceprolong)

        pricechange = response.xpath('//*[@id="show_domain"]/div/div/table/tbody/tr[1]/td[5]/a/text()').get()
        pricechange = str(pricechange).strip()
        if m := re.match(REGEX_PATTERN, pricechange):
            pricechange = m.group(1)
            pricechange = f'{float(pricechange)}'
            logging.info('pricechange = %s', pricechange)

        item = NsregItem()
        item['name'] = "ООО «Актив.Домэинс»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange 
        item['price'] = price

        yield item
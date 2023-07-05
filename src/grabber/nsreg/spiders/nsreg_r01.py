# -*- coding: utf-8 -*-
import logging
import re

import scrapy
from nsreg.items import NsregItem

from ..utils import find_price_withoutre
#работает
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}


class NsregR01Spider(scrapy.Spider):
    name = 'nsreg_r01'
    allowed_domains = ['r01.ru']
    start_urls = ['https://r01.ru/domain/pay/']

    def parse(self, response):
        pricereg = response.xpath('/html/body/table/tr[2]/td[2]/table/tr[4]/td[2]/text()').get()
        pricereg = find_price_withoutre(pricereg)
        
        priceprolong = response.xpath('/html/body/table/tr[2]/td[2]/table/tr[4]/td[3]/text()').get()
        priceprolong = find_price_withoutre(priceprolong)

        pricechange = response.xpath('/html/body/table/tr[2]/td[2]/table/tr[4]/td[4]/text()').get()
        pricechange = find_price_withoutre(pricechange)

        item = NsregItem()
        item['name'] = "ООО «Регистратор Р01»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange 
        item['price'] = price

        yield item

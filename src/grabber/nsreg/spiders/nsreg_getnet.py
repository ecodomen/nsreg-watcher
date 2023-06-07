
# -*- coding: utf-8 -*-
import logging
import re

import scrapy
from nsreg.items import NsregItem

from ..utils import find_price_withoutre
#не работает

EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}

class NsregGetnetSpider(scrapy.Spider):
    name = "nsreg_getnet"
    allowed_domains = ["format.gtn.ee"]
    start_urls = ["https://format.gtn.ee/price"]

    def parse(self, response):
        pricereg = response.xpath('//table[class="tbl-bordered"]').get()
        pricereg = find_price_withoutre(pricereg)
        
        priceprolong = response.xpath('//tbody/tr[3]/td[2]/text()').get()
        priceprolong = find_price_withoutre(priceprolong)

        pricechange = response.xpath('//tbody/tr[4]/td[2]/text()').get()
        pricechange = find_price_withoutre(pricechange)

        item = NsregItem()
        item['name'] = "ООО «ГЕТ-НЭТ»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange 
        item['price'] = price

        yield item

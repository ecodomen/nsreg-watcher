# -*- coding: utf-8 -*-
import scrapy
from nsreg.items import NsregItem

from ..utils import find_price
REGEX_PATTERN = r"([0-9]+[.,\s])?руб"
EMPTY_PRICE = {
    'pricereg': None,
    'price_prolong': None,
    'price_change': None,
}

class NsregTimewebSpider(scrapy.Spider):
    name = 'nsreg_timeweb'
    allowed_domains = ['timeweb.name']
    start_urls = ['https://timeweb.name/tariff']


    def parse(self, response):
        pricereg = response.xpath('/html/body/div/section/div/table/tbody/tr/td[1]/text()').get()
        pricereg = find_price(REGEX_PATTERN, pricereg)

        price_prolong = response.xpath('/html/body/div/section/div/table/tbody/tr[1]/td[1]/text()').get()
        price_prolong = find_price(REGEX_PATTERN, price_prolong)

        price_change = response.xpath('/html/body/div/section/div/table/tbody/tr[2]/td[1]/text()').get()
        price_change = find_price(REGEX_PATTERN, price_change)

        item = NsregItem()
        item['name'] = "ООО «ТаймВэб.Домены»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['price_prolong'] = price_prolong
        price['price_change'] = price_change
        item['price'] = price

        yield item

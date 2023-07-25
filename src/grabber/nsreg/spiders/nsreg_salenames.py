# -*- coding: utf-8 -*-
import scrapy
from nsreg.items import NsregItem

from ..utils import find_price_withoutre
# работает
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}


class NsregSalenamesSpider(scrapy.Spider):
    name = 'nsreg_salenames'
    allowed_domains = ['www.salenames.ru']
    start_urls = ['https://www.salenames.ru/ru/page/tarify']

    def parse(self, response):
        pricereg = response.xpath(
            '//*[@id="content"]/div/div/table[1]/tbody/tr[1]/td[2]/text()').get()
        pricereg = find_price_withoutre(pricereg)

        priceprolong = response.xpath(
            '//*[@id="content"]/div/div/table[1]/tbody/tr[2]/td[2]/text()').get()
        priceprolong = find_price_withoutre(priceprolong)

        pricechange = response.xpath(
            '//*[@id="content"]/div/div/table[1]/tbody/tr[3]/td[2]/text()').get()
        pricechange = find_price_withoutre(pricechange)

        item = NsregItem()
        item['name'] = "ООО «СэйлНэймс»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange
        item['price'] = price

        yield item

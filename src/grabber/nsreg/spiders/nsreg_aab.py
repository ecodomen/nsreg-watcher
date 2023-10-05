# -*- coding: utf-8 -*-
import scrapy
from nsreg.items import NsregItem

from ..utils import find_price_withoutre
# работает

EMPTY_PRICE = {
    'price_reg': None,
    'price_prolong': None,
    'price_change': None,
}


class Nsreg_aabSpider(scrapy.Spider):
    name = 'nsreg_aab'
    allowed_domains = ['aab.ru']
    start_urls = ['https://aab.ru/tarifi_na_uslugi.html']

    def parse(self, response):
        price_reg = response.xpath(
            '//*[@id="full_story"]/table/tbody/tr[3]/td[2]/text()').get()
        price_reg = find_price_withoutre(price_reg)

        price_prolong = response.xpath(
            '//*[@id="full_story"]/table/tbody/tr[6]/td[2]/text()').get()
        price_prolong = find_price_withoutre(price_prolong)

        price_change = response.xpath(
            '//*[@id="full_story"]/table/tbody/tr[9]/td[2]/text()').get()
        price_change = find_price_withoutre(price_change)

        item = NsregItem()
        item['name'] = "ООО «ААБ Медиа»"
        price = item.get('price', EMPTY_PRICE)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        price['price_change'] = price_change
        item['price'] = price

        yield item

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


class NsregR01Spider(scrapy.Spider):
    name = 'nsreg_r01'
    allowed_domains = ['r01.ru']
    start_urls = ['https://r01.ru/domain/pay/']

    def parse(self, response):
        price_reg = response.xpath(
            '/html/body/table/tr[2]/td[2]/table/tr[4]/td[2]/text()').get()
        price_reg = find_price_withoutre(price_reg)

        price_prolong = response.xpath(
            '/html/body/table/tr[2]/td[2]/table/tr[4]/td[3]/text()').get()
        price_prolong = find_price_withoutre(price_prolong)

        price_change = response.xpath(
            '/html/body/table/tr[2]/td[2]/table/tr[4]/td[4]/text()').get()
        price_change = find_price_withoutre(price_change)

        item = NsregItem()
        item['name'] = "ООО «Регистратор Р01»"
        price = item.get('price', EMPTY_PRICE)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        price['price_change'] = price_change
        item['price'] = price

        yield item

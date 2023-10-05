# -*- coding: utf-8 -*-
import scrapy
from nsreg.items import NsregItem

from ..utils import find_price_sub
# работает

REGEX_PATTERN = r".*([0-9]+[\s][0-9]{3}).*"
EMPTY_PRICE = {
    'price_reg': None,
    'price_prolong': None,
    'price_change': None,
}


class NsregAltnamesSpider(scrapy.Spider):
    name = 'nsreg_altnames'
    allowed_domains = ['altnames.ru']
    start_urls = ['http://altnames.ru/']

    def parse(self, response):
        price_reg = response.xpath(
            '//*[@id="post-10"]/div/div/div/div/section[4]/div/div/div/div[2]/div/table/tbody/tr[1]/td[2]/text()').get()
        price_reg = find_price_sub(REGEX_PATTERN, price_reg)

        price_prolong = response.xpath(
            '//*[@id="post-10"]/div/div/div/div/section[4]/div/div/div/div[2]/div/table/tbody/tr[2]/td[2]/text()').get()
        price_prolong = find_price_sub(REGEX_PATTERN, price_prolong)

        price_change = response.xpath(
            '//*[@id="post-10"]/div/div/div/div/section[4]/div/div/div/div[2]/div/table/tbody/tr[3]/td[2]/text()').get()
        price_change = find_price_sub(REGEX_PATTERN, price_change)

        item = NsregItem()
        item['name'] = "ООО «АЛЬТЕРНАТИВА»"
        price = item.get('price', EMPTY_PRICE)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        price['price_change'] = price_change
        item['price'] = price

        yield item

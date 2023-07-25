# -*- coding: utf-8 -*-
import scrapy
from nsreg.items import NsregItem

from ..utils import find_price
# работает

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
        pricereg = response.xpath(
            '//*[@id="show_domain"]/div/div/table/tbody/tr[1]/td[3]/a/text()').get()
        pricereg = find_price(REGEX_PATTERN, pricereg)

        priceprolong = response.xpath(
            '//*[@id="show_domain"]/div/div/table/tbody/tr[1]/td[4]/a/text()').get()
        priceprolong = find_price(REGEX_PATTERN, priceprolong)

        pricechange = response.xpath(
            '//*[@id="show_domain"]/div/div/table/tbody/tr[1]/td[5]/a/text()').get()
        pricechange = find_price(REGEX_PATTERN, pricechange)

        item = NsregItem()
        item['name'] = "ООО «Актив.Домэинс»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange
        item['price'] = price

        yield item

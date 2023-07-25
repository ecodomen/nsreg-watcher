# -*- coding: utf-8 -*-
import scrapy
from nsreg.items import NsregItem

from ..utils import find_price
# работает
REGEX_PATTERN = r"([0-9]+)[.,\s]?руб.*"
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}


class NsregDomainshopSpider(scrapy.Spider):
    name = "nsreg_domainshop"
    allowed_domains = ["domainshop.ru"]
    start_urls = ["https://domainshop.ru/services/"]

    def parse(self, response):
        pricereg = response.xpath(
            '/html/body/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr[1]/td[2]/div/text()').get()
        pricereg = find_price(REGEX_PATTERN, pricereg)

        priceprolong = response.xpath(
            '/html/body/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr[4]/td[2]/div/p/text()').get()
        priceprolong = find_price(REGEX_PATTERN, priceprolong)

        pricechange = response.xpath(
            '/html/body/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr[7]/td[2]/div/text()').get()
        pricechange = find_price(REGEX_PATTERN, pricechange)

        item = NsregItem()
        item['name'] = "ООО «Лавка доменов»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange
        item['price'] = price

        yield item

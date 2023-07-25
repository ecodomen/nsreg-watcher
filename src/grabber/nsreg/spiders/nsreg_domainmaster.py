# -*- coding: utf-8 -*-
import scrapy
from nsreg.items import NsregItem

from ..utils import find_price
# работает
REGEX_PATTERN = r"([0-9]+[.,\s])?руб"
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}


class NsregDomainmasterSpider(scrapy.Spider):
    name = "nsreg_domainmaster"
    allowed_domains = ["domainmaster.ru"]
    start_urls = ["https://domainmaster.ru/site/tariffs"]

    def parse(self, response):
        pricereg = response.xpath(
            '/html/body/section/div/div/div/div[2]/div[1]/div[2]/span/text()').get()
        pricereg = find_price(REGEX_PATTERN, pricereg)

        priceprolong = response.xpath(
            '/html/body/section/div/div/div/div[2]/div[2]/div[2]/span/text()').get()
        priceprolong = find_price(REGEX_PATTERN, priceprolong)

        pricechange = response.xpath(
            '/html/body/section/div/div/div/div[2]/div[3]/div[2]/span/text()').get()
        pricechange = find_price(REGEX_PATTERN, pricechange)

        item = NsregItem()
        item['name'] = "ООО «Доменный Мастер»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange
        item['price'] = price

        yield item

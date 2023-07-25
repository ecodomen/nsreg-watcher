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


class NsregMasterhostSpider(scrapy.Spider):
    name = "nsreg_masterhost"
    allowed_domains = ["masterhost.ru"]
    start_urls = ["https://masterhost.ru/domain/price/"]

    def parse(self, response):
        pricereg = response.xpath(
            '//*[@id="app"]/section[1]/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/span/span/text()').get()
        pricereg = find_price(REGEX_PATTERN, pricereg)

        priceprolong = response.xpath(
            '//*[@id="app"]/section[1]/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/span/text()').get()
        priceprolong = find_price(REGEX_PATTERN, priceprolong)

        pricechange = None

        item = NsregItem()
        item['name'] = "ООО «МАСТЕРХОСТ»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange
        item['price'] = price

        yield item

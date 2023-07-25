# -*- coding: utf-8 -*-
import scrapy
from nsreg.items import NsregItem

from ..utils import find_price
# работает
REGEX_PATTERN = r".*(([0-9]*[.,])?[0-9]{3})₽.*"
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}


class NsregRfSpider(scrapy.Spider):
    name = "nsreg_rf"
    allowed_domains = ["rf.ru"]
    start_urls = ["https://rf.ru/domain-prices"]

    def parse(self, response):
        pricereg = response.xpath(
            '//*[@id="wrapper"]/section[1]/div/table/tbody/tr[1]/td[2]/text()').get()
        pricereg = find_price(REGEX_PATTERN, pricereg)

        priceprolong = response.xpath(
            '//*[@id="wrapper"]/section[1]/div/table/tbody/tr[1]/td[3]/text()').get()
        priceprolong = find_price(REGEX_PATTERN, priceprolong)

        pricechange = response.xpath(
            '//*[@id="wrapper"]/section[1]/div/table/tbody/tr[1]/td[4]/text()').get()
        pricechange = find_price(REGEX_PATTERN, pricechange)

        item = NsregItem()
        item['name'] = "ООО «ДОМЕНЫ.РФ»"
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        price['pricechange'] = pricechange
        item['price'] = price

        yield item

# -*- coding: utf-8 -*-
import scrapy
from ..utils import find_price
from nsreg.items import NsregItem

REGEX_PATTERN = r"₽\s*([0-9]+\.[0-9]+)\s*RUB"
EMPTY_PRICE = {
    'price_reg': None,
    'price_prolong': None,
    'price_change': None,
}


class NsregElastichostingSpider(scrapy.Spider):
    name = "nsreg_elastichosting"
    start_urls = ["https://elastichosting.ru/domain/pricing"]
    allowed_domains = ["elastichosting.ru"]

    def parse(self, response):
        price_reg = response.xpath(
            '//tr[.//strong[.=".ru"]]/td[contains(., "New Price")]/text()').getall()[1].strip()
        price_prolong = response.xpath(
            '//tr[.//strong[.=".ru"]]/td[contains(., "Renewal")]/text()').getall()[1].strip()
        price_change = response.xpath(
            '//tr[.//strong[.=".ru"]]/td[contains(., "Transfer")]/text()').getall()[1].strip()

        item = NsregItem()
        item['name'] = "ООО «ЭластикХостинг»"
        price = item.get('price', EMPTY_PRICE)
        price['price_reg'] = find_price(REGEX_PATTERN, price_reg)
        price['price_prolong'] = find_price(REGEX_PATTERN, price_prolong)
        price['price_change'] = find_price(REGEX_PATTERN, price_change)
        item['price'] = price

        yield item

# -*- coding: utf-8 -*-
import scrapy
from nsreg.items import NsregItem

from ..utils import find_price_withoutre
# не работает

EMPTY_PRICE = {
    'price_reg': None,
    'price_prolong': None,
    'price_change': None,
}


class NsregGetnetSpider(scrapy.Spider):
    name = "nsreg_getnet"
    allowed_domains = ["format.gtn.ee"]
    start_urls = ["https://format.gtn.ee/price"]

    def parse(self, response):
        price_reg = response.xpath('//table[class="tbl-bordered"]').get()
        price_reg = find_price_withoutre(price_reg)

        price_prolong = response.xpath('//tbody/tr[3]/td[2]/text()').get()
        price_prolong = find_price_withoutre(price_prolong)

        price_change = response.xpath('//tbody/tr[4]/td[2]/text()').get()
        price_change = find_price_withoutre(price_change)

        item = NsregItem()
        item['name'] = "ООО «ГЕТ-НЭТ»"
        price = item.get('price', EMPTY_PRICE)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        price['price_change'] = price_change
        item['price'] = price

        yield item

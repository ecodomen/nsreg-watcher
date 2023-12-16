# -*- coding: utf-8 -*-
import scrapy


from nsreg.items import NsregItem

from ..utils import find_price_sub

REGEX_PATTERN = r".*([0-9]+\s[0-9]*)₽"
EMPTY_PRICE = {
    "price_reg": None,
    "price_prolong": None,
    "price_change": None,
}


class NsregCapnamesSpider(scrapy.Spider):
    name = "nsreg_capnames.py"
    start_urls = ["https://capnames.ru/"]
    allowed_domains = "capnames.ru"

    def parse(self, response):
        price_reg = response.xpath(
            "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div[2]/div/p[1]/text()"
        )
        price_reg = find_price_sub(REGEX_PATTERN, price_reg)

        price_prolong = response.xpath(
            "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/p[1]/text()"
        )
        price_prolong = find_price_sub(REGEX_PATTERN, price_prolong)

        price_change = response.xpath(
            "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div[3]/div/div/div[2]/div/p[1]/text()"
        )
        price_change = find_price_sub(REGEX_PATTERN, price_change)

        item = NsregItem()
        item["name"] = "ООО «КАПИТАЛЪ»"
        price = item.get("price", EMPTY_PRICE)
        price["price_reg"] = price_reg
        price["price_prolong"] = price_prolong
        price["price_change"] = price_change
        item["price"] = price

        yield item

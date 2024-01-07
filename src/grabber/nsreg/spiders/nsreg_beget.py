# -*- coding: utf-8 -*-
import scrapy
from nsreg.items import NsregItem

from ..utils import find_price

# работает, добавлен парс переноса с другой страницы.

REGEX_PATTERN = r"([0-9]{3,}).*"
REGEX_CHANGE_PATTERN = r".*?(\d+)\s*рублей.*"

EMPTY_PRICE = {
    "price_reg": None,
    "price_prolong": None,
    "price_change": None,
}


class NsregBegetSpider(scrapy.Spider):
    name = "nsreg_beget"
    allowed_domains = ["beget.com"]
    start_urls = ["https://beget.com/ru/domains/zone/ru"]

    def parse_price_change(self, response):
        price_change = response.xpath(
            '//*[@id="__layout"]/div/div[3]/div[1]/div/div/div/div[3]/div[2]/div/div[1]/ul[3]/li[1]/text()'
        ).get()
        price_change = find_price(REGEX_CHANGE_PATTERN, price_change)

        item = NsregItem()
        item["name"] = "ООО «Бегет»"
        price = item.get("price", EMPTY_PRICE)
        price["price_change"] = price_change
        item["price"] = price

        yield item

    def parse(self, response):
        price_reg = response.xpath(
            '//*[@id="__layout"]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/p[2]/text()'
        ).get()
        price_reg = find_price(REGEX_PATTERN, price_reg)

        price_prolong = response.xpath(
            '//*[@id="__layout"]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[2]/p[2]/text()'
        ).get()
        price_prolong = find_price(REGEX_PATTERN, price_prolong)

        item = NsregItem()
        item["name"] = "ООО «Бегет»"
        price = item.get("price", EMPTY_PRICE)
        price["price_reg"] = price_reg
        price["price_prolong"] = price_prolong
        item["price"] = price

        yield scrapy.Request(
            "https://beget.com/ru/kb/how-to/domains/kak-perenesti-domeny-v-beget",
            callback=self.parse_price_change,
        )

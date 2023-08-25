# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import find_price, PRICE_DEFAULT_DICT
from ..items import NsregItem


class NsregWebnamesSpider(scrapy.Spider):
    name = "nsreg_webnames"
    allowed_domains = ("www.webnames.ru", )
    start_urls = ("https://www.webnames.ru/tld/catalog/ru", )
    site_name = 'ООО «Регтайм»'

    page_price_change = "https://www.webnames.ru/perenos-domena-ot-drugogo-registratora-v-webnames-ru"

    def parse(self, response):
        price_reg = response.xpath('/html/body/section[1]/div[4]/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/strong/text()').get()
        price_reg = find_price(r"([0-9]+)", price_reg)

        price_prolong = response.xpath('/html/body/section[1]/div[4]/div[1]/div[2]/div/table/tbody/tr[3]/td[2]/strong/text()').get()
        price_prolong = find_price(r"([0-9]+)", price_prolong)

        # Переходим на другую страницу для сбора информации
        yield scrapy.Request(url=self.page_price_change, callback=self.parse_change,
                             cb_kwargs={"price_reg": price_reg,
                                        "price_prolong": price_prolong})

    def parse_change(self, response, price_reg, price_prolong):
        price_change = response.xpath('/html/body/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/span/text()').get()
        price_change = find_price(r"([0-9]+)", price_change)

        # Создаем Item для сайта
        item = NsregItem()
        item['name'] = self.site_name
        price = item.get('price', PRICE_DEFAULT_DICT)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        price['price_change'] = price_change
        item['price'] = price

        # Возвращаем готовый Item
        return item

# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent, EMPTY_PRICE, find_price
from ..items import NsregItem

REGEX_PATTERN = r"\.\w+:\s*([\d\s]+)₽"


class NsregStarnamesSpider(scrapy.Spider):
    name = "nsreg_starnames"
    start_urls = ["https://starnames.ru/", ]
    allowed_domains = ("starnames.ru")
    site_names = ("ООО «СтарНэймс»",)

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=REGEX_PATTERN,
            path={
                'price_reg': '/html/body/div/div[2]/div/div[1]/div/div/div[1]/div/p/text()',
                'price_prolong': '/html/body/div/div[2]/div/div[1]/div/div/div[2]/div/p/text()',
                'price_change': '/html/body/div/div[2]/div/div[1]/div/div/div[3]/div/p/text()'
            }
        )

    def find_price(self, re_pattern, price_text):
        price_text = price_text.replace(' ', '')
        return find_price(re_pattern, price_text)

    def parse(self, response):

        # Поиск цены на регистрацию домена на веб-странице
        price_reg = response.xpath(self.component.path['price_reg']).get()
        price_reg = self.find_price(self.component.regex['price_reg'], price_reg)

        # Поиск цены на изменение домена на веб-странице
        price_prolong = response.xpath(self.component.path['price_prolong']).get()
        price_prolong = self.find_price(self.component.regex['price_prolong'], price_prolong)

        # Определение имени сайта (убедитесь, что это работает корректно)
        price_change = response.xpath(self.component.path['price_change']).get()
        price_change = self.find_price(self.component.regex['price_change'], price_change)

        # Получение имя сайта
        site_name = self.component.site_names[self.component.start_urls.index(response.url)]

        # Создание элемента данных и заполнение его информацией
        item = NsregItem()
        item['name'] = site_name
        price = item.get('price', EMPTY_PRICE)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        price['price_change'] = price_change
        item['price'] = price

        return item

# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import find_price, PRICE_DEFAULT_DICT
from ..items import NsregItem


class NsregDomainsNethouseSpider(scrapy.Spider):
    name = "nsreg_domainsnethouse"
    allowed_domains = ("domains.nethouse.ru", )
    start_urls = ("https://domains.nethouse.ru/help/1/8", )
    site_name = 'ООО «Регистрант»'

    def parse(self, response):

        # Цены на перевод сайта от другого регистратора при вводе домена
        price_reg = response.xpath('/html/body/main/section/div/div/article/div[1]/div/table/tbody/tr[1]/td[2]/text()').get()
        price_reg = find_price(r"([0-9]+)", price_reg)

        price_prolong = response.xpath('/html/body/main/section/div/div/article/div[1]/div/table/tbody/tr[1]/td[2]/span/text()').get()
        price_prolong = find_price(r"([0-9]+)", price_prolong)

        # Создаем Item для сайта
        item = NsregItem()
        item['name'] = self.site_name
        price = item.get('price', PRICE_DEFAULT_DICT)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        item['price'] = price

        # Возвращаем готовый Item
        return item

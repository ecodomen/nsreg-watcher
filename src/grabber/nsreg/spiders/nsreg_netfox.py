# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import find_price, PRICE_DEFAULT_DICT
from ..items import NsregItem


class NsregNetfoxSpider(scrapy.Spider):
    name = "nsreg_netfox"
    allowed_domains = ("www.netfox.ru", )
    start_urls = ("https://netfox.ru/domains/", )
    site_name = 'ООО «НЕТФОКС»'

    def parse(self, response):

        # Цены на продление и перевод сайта от другого регистратора в docx файле
        price_reg = response.xpath('//*[@id="bbody"]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/strong/text()').get()
        price_reg = find_price(r"([0-9]+)", price_reg)

        # Создаем Item для сайта
        item = NsregItem()
        item['name'] = self.site_name
        price = item.get('price', PRICE_DEFAULT_DICT)
        price['price_reg'] = price_reg
        item['price'] = price

        # Возвращаем готовый Item
        return item

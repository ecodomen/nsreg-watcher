# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import find_price, PRICE_DEFAULT_DICT
from ..items import NsregItem


class NsregDomenusSpider(scrapy.Spider):
    name = "nsreg_domenus"
    allowed_domains = ("www.domenus.ru", )
    start_urls = ("https://www.domenus.ru/price", )
    site_name = 'ООО "РЕГИСТРАТОР"'

    page_price_change = "https://www.domenus.ru/support/help/group/1343472/question/perenos-domenov-ru-su-rf-k-registratoru-domenus-ru-ot-drugogo-registratora"

    def parse(self, response):
        price_reg = response.xpath('/html/body/main/div[1]/div/div[3]/table/tbody/tr[321]/td[2]/span/text()').get()
        # Заменяем "," на ".", чтобы сработал перевод в тип float
        price_reg = price_reg.replace(",", ".")
        price_reg = find_price(r"([0-9]+[.,\s])?руб", price_reg)

        price_prolong = response.xpath('/html/body/main/div[1]/div/div[3]/table/tbody/tr[321]/td[3]/span/text()').get()
        # Заменяем "," на ".", чтобы сработал перевод в тип float
        price_prolong = price_prolong.replace(",", ".")
        price_prolong = find_price(r"([0-9]+[.,\s])?руб", price_prolong)

        # Переходим на другую страницу для сбора информации
        yield scrapy.Request(url=self.page_price_change, callback=self.parse_change,
                             cb_kwargs={"price_reg": price_reg,
                                        "price_prolong": price_prolong})

    def parse_change(self, response, price_reg, price_prolong):
        price_change = response.xpath('/html/body/main/div[1]/div/div/p[3]/strong/text()').get()
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

# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent, EMPTY_PRICE, find_price
from ..items import NsregItem


class NsregRegruSpider(scrapy.Spider):
    name = "nsreg_regru"
    allowed_domains = ["reg.ru"]
    start_urls = ["https://www.reg.ru/company/retail"]
    site_names = ("ООО «РЕГ.РУ»",)

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9]+)[.,\s]?.*",
            path={
                'price_reg': '/html/body/div[1]/div/div[4]/article/div/div[2]/div[4]/div/table/tbody/tr[1]/td[2]/abbr/strong/text()',
                'price_prolong': '/html/body/div[1]/div/div[4]/article/div/div[2]/div[4]/div/table/tbody/tr[1]/td[2]/abbr/em/text()',
                'price_change': '/html/body/div[1]/div/article/div[3]/div/div[2]'
            }
        )

    def parse_price_change(self, response):
        price_change = response.xpath(self.component.path['price_change']).get()
        price_change = find_price(r"[\s\S]+(\d{3,}) руб.[\s\S]+", price_change)

        item = NsregItem()
        item['name'] = "ООО «РЕГ.РУ»"
        price = item.get('price', EMPTY_PRICE)
        price['price_change'] = price_change
        item['price'] = price

        yield item

    def parse(self, response):

        price_reg = response.xpath(self.component.path['price_reg']).get()
        price_reg = find_price(self.component.regex['price_reg'], price_reg)

        price_prolong = response.xpath(self.component.path['price_prolong']).get()
        price_prolong = find_price(r"/\n\s.*(([0-9]*[.,])?[0-9]{3})", price_prolong)

        yield scrapy.Request(
            'https://help.reg.ru/support/domains/perenos-domena/perenos-domena-v-reg-ru/perenos-domena-v-zonakh-ru-i-rf-ot-drugogo-registratora-v-reg-ru',
            callback=self.parse_price_change)

        item = NsregItem()
        item['name'] = "ООО «РЕГ.РУ»"
        price = item.get('price', EMPTY_PRICE)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        item['price'] = price

        return item

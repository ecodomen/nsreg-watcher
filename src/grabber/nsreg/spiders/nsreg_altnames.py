# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent, EMPTY_PRICE
from ..items import NsregItem

import re
import logging


def find_price_sub(re_pattern, price):
    price = str(price).strip()
    if m := re.match(re_pattern, price):
        price = m.group(1)
        price = re.sub(r'\s', '', price)
        price = f'{float(price)}'
        logging.info('price = %s', price)

        return price


class NsregMaxnameSpider(scrapy.Spider):
    name = 'nsreg_altnames'
    allowed_domains = ['altnames.ru']
    start_urls = ['http://altnames.ru/']
    site_names = ("ООО «АЛЬТЕРНАТИВА»",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r".*([0-9]+[\s][0-9]{3}).*",
            path={
                'price_reg': '//*[@id="post-10"]/div/div/div/div/section[4]/div/div/div/div[2]/div/table/tbody/tr[1]/td[2]/text()',
                'price_prolong': '//*[@id="post-10"]/div/div/div/div/section[4]/div/div/div/div[2]/div/table/tbody/tr[2]/td[2]/text()',
                'price_change': '//*[@id="post-10"]/div/div/div/div/section[4]/div/div/div/div[2]/div/table/tbody/tr[3]/td[2]/text()',
            },
        )

    def parse(self, response):
        price_reg = response.xpath(self.component.path['price_reg']).get()
        price_reg = find_price_sub(self.component.regex['price_reg'], price_reg)

        price_prolong = response.xpath(self.component.path['price_prolong']).get()
        price_prolong = find_price_sub(self.component.regex['price_prolong'], price_prolong)

        price_change = response.xpath(self.component.path['price_change']).get()
        price_change = find_price_sub(self.component.regex['price_change'], price_change)

        item = NsregItem()
        item['name'] = self.site_names[0]
        price = item.get('price', EMPTY_PRICE)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        price['price_change'] = price_change
        item['price'] = price

        return item

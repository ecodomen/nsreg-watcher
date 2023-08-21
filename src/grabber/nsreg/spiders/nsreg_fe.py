# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregFeSpider(scrapy.Spider):
    name = "nsreg_fe"
    start_urls = ["https://fe.ru/domains.php"]
    allowed_domains = ("fe.ru")
    site_names = ("ООО «Регистрация доменов»")

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex={
                'price_reg': r"([0-9]+[.,\s])?руб",
                'price_prolong': r"продление ([0-9]+[.,\s])?руб",
                'price_change': r"(.+)",
            },
            path={
                'price_reg': '/html/body/div[1]/div[4]/div/div[1]/center/table/tr[5]/td[2]/font[1]/text()',
                'price_prolong': '/html/body/div[1]/div[4]/div/div[1]/center/table/tr[5]/td[2]/font[2]/text()',
                'price_change': '/html/body/div[1]/div[4]/div/div[1]/center/table/tr[5]/td[2]/font[3]/text()'
            }
        )

    def parse(self, response):
        return self.component.parse(response)

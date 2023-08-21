# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregRegistrarusSpider(scrapy.Spider):
    name = "nsreg_registrarus"
    start_urls = ["https://registrarus.ru/services/index.html"]
    allowed_domains = ("registrarus.ru")
    site_names = ('ООО "Регистрарус"')

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9]+[.,\s])?руб",
            path={
                'price_reg': '/html/body/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr[1]/td[2]/div/text()',
                'price_prolong': '/html/body/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr[3]/td[2]/div/p/text()',
                'price_change': '/html/body/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr[5]/td[2]/div/text()'
            }
        )

    def parse(self, response):
        return self.component.parse(response)

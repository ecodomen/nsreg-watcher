# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregMasternameSpider(scrapy.Spider):
    name = "nsreg_mastername"
    start_urls = ["https://mastername.ru/service/"]
    allowed_domains = ("mastername.ru")
    site_names = ("ООО «Регистратор доменов»",)

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9]+[.,\s])?руб",
            path={
                'price_reg': '/html/body/div[4]/div/div[1]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/span/text()',
                'price_prolong': '/html/body/div[4]/div/div[1]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[3]/span/text()',
                'price_change': '/html/body/div[4]/div/div[1]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[4]/div/div/span[2]/text()'
            }
        )

    def parse(self, response):
        return self.component.parse(response)

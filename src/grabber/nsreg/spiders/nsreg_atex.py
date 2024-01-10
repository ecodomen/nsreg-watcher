# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregAtexSpider(scrapy.Spider):
    name = "nsreg_atex.py"
    start_urls = ["https://domainshop.ru/services/"]
    allowed_domains = ("atex.ru")
    site_names = ("ООО «Атекс»",)

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9]+[.,\s])?руб",
            path={
                'price_reg': '/html/body/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr[1]/td[2]/div/text()',
                'price_prolong': '/html/body/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr[3]/td[2]/div/text()',
                'price_change': '/html/body/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr[5]/td[2]/div/text()'
            }
        )

    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

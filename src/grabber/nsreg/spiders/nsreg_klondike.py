# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregKlondikeSpider(scrapy.Spider):
    name = "nsreg_klondike.py"
    start_urls = ["https://klondike-studio.ru/domain/prices/"]
    allowed_domains = ("klondike-studio.ru")
    site_names = ("ООО «Клондайк Групп»",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9]+)[.,\s]?руб*",
            path={
                'price_reg': '/html/body/div[2]/section/div/div/table/tbody/tr[1]/td[2]/text()',
                'price_prolong': '/html/body/div[2]/section/div/div/table/tbody/tr[3]/td[2]/text()',
                'price_change': '/html/body/div[2]/section/div/div/table/tbody/tr[5]/td[2]/text()'
            }
        )

    def parse(self, response):
        return self.component.parse(response)

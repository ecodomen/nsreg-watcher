# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregDomenySpider(scrapy.Spider):
    name = "nsreg_domeny.py"
    start_urls = ["https://domeny.ru/pricelist/"]
    allowed_domains = ("domeny.ru")
    site_names = ("ООО «Доменный Мастер»",)

    # Конструктор класса
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r".*(([0-9]*[.,])?[0-9]{3})\s+₽.*",
            path={
                'price_reg': '/html/body/div[2]/section/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/table/tbody/tr[3]/td[2]/text()',
                'price_prolong': '//html/body/div[2]/section/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/table/tbody/tr[3]/td[3]/text()',
                'price_change': '/html/body/div[2]/section/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/table/tbody/tr[2]/td[2]/text()'
            }
        )

    def parse(self, response):
        return self.component.parse(response)

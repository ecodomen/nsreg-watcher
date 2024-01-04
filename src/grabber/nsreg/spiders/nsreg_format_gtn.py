# -*- coding: utf-8 -*-
import scrapy
from ..base_site_spider import BaseSpiderComponent


class FormatGtnSpider(scrapy.Spider):
    name = "nsreg_format_gtn"
    start_urls = ["https://format.gtn.ee/"]
    allowed_domains = ["format.gtn.ee"]
    site_names = ("ООО Гет-Нэт",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex={
               'price_reg': r".*?([0-9]+)*",
               'price_prolong': r".*?([0-9]+)*",
               'price_change': r".*?([0-9]+)*",
            },
            path={
               'price_reg': '/html/body/div/div/div/div[2]/div/div/div/table/tbody/tr[2]/td[2]/text()',
               'price_prolong': '/html/body/div/div/div/div[2]/div/div/div/table/tbody/tr[3]/td[2]/text()',
               'price_change': '/html/body/div/div/div/div[2]/div/div/div/table/tbody/tr[4]/td[2]/text()'
            }
        )

    def parse(self, response):
        return self.component.parse(response)

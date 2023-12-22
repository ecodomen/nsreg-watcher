# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent

REGEX_PATTERN = r".*([0-9]+\s[0-9]*)₽"


class NsregCapnamesSpider(scrapy.Spider):
    name = "nsreg_capnames.py"
    start_urls = ["https://capnames.ru/"]
    allowed_domains = "capnames.ru"
    site_names = ("ООО «КАПИТАЛЪ»",)

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=REGEX_PATTERN,
            path={
                "price_reg": "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div[2]/div/p[1]/text()",
                "price_prolong": "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/p[1]/text()",
                "price_change": "/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div[3]/div/div/div[2]/div/p[1]/text()",
            },
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

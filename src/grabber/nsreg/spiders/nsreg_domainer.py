# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


# Пример спайдера для одного сайта
class NsregDomainerSpider(scrapy.Spider):
    name = "nsreg_domainer"
    start_urls = ["https://domainer.ru/info/services"]
    allowed_domains = ("domainer.ru")
    site_names = ("ООО «Домейнер»")

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9]?[0-9]+[.,\s])?руб",
            path={
                'price_reg': '/html/body/div[2]/table/tbody/tr[1]/td[2]/text()',
                'price_prolong': '/html/body/div[2]/table/tbody/tr[1]/td[2]/text()',
                'price_change': '/html/body/div[2]/table/tbody/tr[3]/td[2]/text()'
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

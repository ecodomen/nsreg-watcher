# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


# Пример спайдера для одного сайта
class NsregZonadomenovSpider(scrapy.Spider):
    name = "nsreg_zonadomenov"
    start_urls = ["https://zonadomenov.ru/site/tariffs"]
    allowed_domains = ("zonadomenov.ru")
    site_names = ("ООО «Зона Доменов»",)

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9]+[.,\s])?руб",
            path={
                'price_reg': '/html/body/section/div/div/div/div[2]/div[1]/div[2]/span/text()',
                'price_prolong': '/html/body/section/div/div/div/div[2]/div[2]/div[2]/span/text()',
                'price_change': '/html/body/section/div/div/div/div[2]/div[3]/div[2]/span/text()'
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

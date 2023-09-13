# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


# Пример спайдера для одного сайта
class NsregWebnamesSpider(scrapy.Spider):
    name = "nsreg_webnames"
    start_urls = ["https://www.webnames.ru/tld/catalog/ru"]
    allowed_domains = ("www.webnames.ru")
    site_names = ("ООО «Зона Доменов»")

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9]+[.,\s])?₽",
            path={
                'price_reg': '/html/body/section[1]/div[4]/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/strong/text()',
                'price_prolong': '/html/body/section[1]/div[4]/div[1]/div[2]/div/table/tbody/tr[3]/td[2]/strong/text()',
                'price_change': None
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

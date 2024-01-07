# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregPinSpbSpider(scrapy.Spider):
    name = "nsreg_pinspb.py"
    start_urls = ["https://pinspb.ru/domains/prices/"]
    allowed_domains = ("pinspb.ru")
    site_names = ("ООО «ПИН»",)

    # Конструктор класса
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Инициализация компонента BaseSpiderComponent с требуемыми параметрами
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9]+)[.,\s]?руб.*",
            path={
                'price_reg': '/html/body/div[6]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/text()',
                'price_prolong': '/html/body/div[6]/div[1]/div[2]/table/tbody/tr[3]/td[2]/div/text()',
                'price_change': '/html/body/div[6]/div[1]/div[2]/table/tbody/tr[5]/td[2]/div/text()'
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

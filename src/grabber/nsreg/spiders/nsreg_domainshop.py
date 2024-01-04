# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregDomainshopSpider(scrapy.Spider):
    name = "nsreg_domainshop.py"
    start_urls = ["https://domainshop.ru/services/"]
    allowed_domains = ["domainshop.ru"]
    site_names = ("ООО «Лавка доменов»",)

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
                'price_reg': '/html/body/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr[1]/td[2]/div/text()',
                'price_prolong': '/html/body/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr[4]/td[2]/div/p/text()',
                'price_change': '/html/body/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr[7]/td[2]/div/text()'
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

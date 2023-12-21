# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregСetisregSpider(scrapy.Spider):
    name = "nsreg_cetisreg"
    start_urls = ["https://www.cetis-reg.ru/price/"]
    allowed_domains = ("www.cetis-reg.ru")
    site_names = ("ООО «ЦЭТИС»",)

    # Конструктор класса
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Инициализация компонента BaseSpiderComponent с требуемыми параметрами
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex={
                'price_reg': r".*?([0-9]+)\s*руб.*",
                'price_prolong': r".*?([0-9]+)\s*руб.*",
                'price_change': r".*?(бесплатно).*",
            },
            path={
                'price_reg': '/html/body/div[1]/div[3]/article/section/table[1]/tr/td[1]/article[1]/div/table/tr[4]/td[2]/text()',
                'price_prolong': '/html/body/div[1]/div[3]/article/section/table[1]/tr/td[1]/article[1]/div/table/tr[4]/td[3]/text()',
                'price_change': '/html/body/div[1]/div[3]/article/section/table[2]/tr/td[1]/article[2]/div/table/tr[10]/td[2]/text()'
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

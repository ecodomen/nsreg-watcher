# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregR01Spider(scrapy.Spider):
    name = "nsreg_r01.py"
    start_urls = ["https://r01.ru/domain/pay/"]
    allowed_domains = ("r01.ru")
    site_names = ("ООО «Регистратор Р01»",)

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
                'price_reg': '/html/body/table/tr[2]/td[2]/table/tr[4]/td[2]/text()',
                'price_prolong': '/html/body/table/tr[2]/td[2]/table/tr[4]/td[3]/text()',
                'price_change': '/html/body/table/tr[2]/td[2]/table/tr[4]/td[4]/text()'
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)


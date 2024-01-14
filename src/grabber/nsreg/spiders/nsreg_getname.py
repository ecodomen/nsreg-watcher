# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregGetnameSpider(scrapy.Spider):
    name = "nsreg_getname.py"
    start_urls = ["http://getname.ru/reg/price/"]
    allowed_domains = ("getname.ru")
    site_names = ("ООО «Элвис-Телеком»",)

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
                'price_reg': '/html/body/table/tr[6]/td[2]/table[2]/tr[3]/td[2]/text()',
                'price_prolong': '//html/body/table/tr[6]/td[2]/table[2]/tr[5]/td[2]/text()',
                'price_change': '/html/body/table/tr[6]/td[2]/table[2]/tr[7]/td[2]/text()'
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

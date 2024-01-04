# -*- coding: utf-8 -*-
import scrapy
import logging
from ..base_site_spider import BaseSpiderComponent


class NsregDomainshopSpider(scrapy.Spider):
    name = "nsreg_openprovider.py"
    start_urls = ["https://www.openprovider.com/ru/prices-for-domains-in-ru"]
    allowed_domains = ("openprovider.com")
    site_names = ("ОПЕНПРОВАЙДЕР, ООО",)

    # Конструктор класса
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Инициализация компонента BaseSpiderComponent с требуемыми параметрами
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r'.*?(\d+).*?',
            path={
                'price_reg': '/html/body/div/div[1]/main/div[2]/div[2]/section/div[3]/ul/li[2]/text()',
                'price_prolong': '/html/body/div/div[1]/main/div[2]/div[2]/section/div[3]/ul/li[3]/text()',
                'price_change': '/html/body/div/div[1]/main/div[2]/div[2]/section/div[3]/ul/li[4]/text()'
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        result = self.component.parse(response)
        logging.info(result)  # Использование logging для вывода результата в консоль
        return result

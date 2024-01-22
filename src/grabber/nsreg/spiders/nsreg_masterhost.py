# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregMasterhostSpider(scrapy.Spider):
    name = "nsreg_masterhost"
    start_urls = ["https://masterhost.ru/domain/"]
    allowed_domains = ("masterhost.ru",)
    site_names = ("ООО «МАСТЕРХОСТ»",)

    # Конструктор класса
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Инициализация компонента BaseSpiderComponent с требуемыми параметрами
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex={
                'price_reg': r"(\d+[.,]?)\d{0,2}",
                'price_prolong': r"(\d+[.,]?)\d{0,2}",
                'price_change': "Бесплатный"
            },

            path={
                'price_reg': '//div[@class="priceBox"][1]//span[@class="text-light"]/text()',
                'price_prolong': '//div[@class="action-holder"][1]//span[@class="text-light"]/text()',
                'price_change': '//li[@class="reset-list-margin"][3]/text()'
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

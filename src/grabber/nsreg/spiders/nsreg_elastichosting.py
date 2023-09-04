# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


# Пример спайдера для одного сайта
class NsregElastichostingSpider(scrapy.Spider):
    name = "nsreg_elastichosting"
    start_urls = ["https://elastichosting.ru/domain/pricing/"]
    allowed_domains = ("elastichosting.ru")
    site_names = ("ООО «Зона Доменов»")

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"₽\s([0-9]{3,})[.,\s]",
            path={
                'price_reg': '//*[@id="tableDomainPricing"]/tbody/tr[20]/td[3]/text()',
                'price_prolong': '//*[@id="tableDomainPricing"]/tbody/tr[20]/td[4]/text()',
                'price_change': '//*[@id="tableDomainPricing"]/tbody/tr[20]/td[5]/text()'
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

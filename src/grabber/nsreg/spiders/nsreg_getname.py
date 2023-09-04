# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


# Пример спайдера для одного сайта
class NsregGetnameSpider(scrapy.Spider):
    name = "nsreg_getname"
    start_urls = ["http://www.getname.ru/reg/price.phtml"]
    allowed_domains = ("www.getname.ru")
    site_names = ("ООО «Элвис-Телеком»")

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9]+[.,\s])?руб",
            path={
                'price_reg': '/html/body/table/tbody/tr[6]/td[2]/table[2]/tbody/tr[3]/td[2]/text()',
                'price_prolong': '/html/body/table/tbody/tr[6]/td[2]/table[2]/tbody/tr[5]/td[2]/text()',
                'price_change': '/html/body/table/tbody/tr[6]/td[2]/table[2]/tbody/tr[5]/td[2]/text()'
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

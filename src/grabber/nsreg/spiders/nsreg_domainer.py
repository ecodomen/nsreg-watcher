# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregDomainshopSpider(scrapy.Spider):
    name = "nsreg_domainer"
    start_urls = ["https://domainer.ru/info/services"]
    allowed_domains = ["domainer.ru",]
    site_names = ("ООО «Домейнер»",)

    # Конструктор класса
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Инициализация компонента BaseSpiderComponent с требуемыми параметрами
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"(\d+)",
            path={
                'price_reg':        'translate(/html/body/div[2]/table/tbody/tr[1]/td[2]/text(), " ", "")',
                'price_prolong':    'translate(/html/body/div[2]/table/tbody/tr[1]/td[2]/text(), " ", "")',
                'price_change':     'translate(/html/body/div[2]/table/tbody/tr[3]/td[2]/text(), " ", "")',
            },
        )

    def parse(self, response):
        return self.component.parse(response)

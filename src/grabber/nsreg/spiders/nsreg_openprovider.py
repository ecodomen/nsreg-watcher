import scrapy

from ..base_site_spider import BaseSpiderComponent

# Пример спайдера для одного сайта
class NsregOpenproviderSpider(scrapy.Spider):
    name = "nsreg_openprovider"
    start_urls = ["https://www.openprovider.com/ru/prices-for-domains-in-ru"]
    allowed_domains = ("www.openprovider.com")
    site_names = ("ООО «Опенпровайдер»")

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9]+).*",
            path={
                'price_reg': '//*[@id="regru"]/section/div[3]/ul/li[2]/text()',
                'price_prolong': '//*[@id="regru"]/section/div[3]/ul/li[3]/text()',
                'price_change': '//*[@id="regru"]/section/div[3]/ul/li[4]/text()'
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)


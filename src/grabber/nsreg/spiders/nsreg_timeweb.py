import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregTimewebSpider(scrapy.Spider):
    name = 'nsreg_timeweb.py'
    allowed_domains = ['timeweb.name']
    start_urls = ['https://timeweb.name/tariff']
    site_names = ("ООО «ТаймВэб.Домены»",)

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
                'price_reg': '/html/body/div/section/div/table/tbody/tr/td[1]/text()',
                'price_prolong': '/html/body/div/section/div/table/tbody/tr[1]/td[1]/text()',
                'price_change': '/html/body/div/section/div/table/tbody/tr[2]/td[1]/text()'
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        return self.component.parse(response)

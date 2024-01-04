import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregSpacewebdomainsSpider(scrapy.Spider):
    name = 'nsreg_spacewebdomains_spider'

    start_urls = ['https://spacewebdomains.ru/%D1%82%D0%B0%D1%80%D0%B8%D1%84%D1%8B/']
    allowed_domains = 'spacewebdomains.ru'
    site_names = 'ООО «СпейсВэб»'

    # Конструктор класса
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Инициализация компонента BaseSpiderComponent с требуемыми параметрами
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            # regex=r"([0-9]+)[.,\s]?руб.*",
            path={
                'price_reg': '/html/body/div[1]/div/div[1]/main/article/div/div/figure/table/tbody/tr[2]/td[2]/text()',
                'price_prolong': '/html/body/div[1]/div/div[1]/main/article/div/div/figure/table/tbody/tr[3]/td[2]/text()',
                'price_change': '/html/body/div[1]/div/div[1]/main/article/div/div/figure/table/tbody/tr[4]/td[2]/text()'
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

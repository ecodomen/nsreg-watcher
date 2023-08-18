import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregAxelnameSpider(scrapy.Spider):
    name = 'nsreg_axelname_spider'

    start_urls = 'https://axelname.ru/domains/'
    allowed_domains = 'https://active.domains'
    site_names = 'ООО «Актив.Домэинс»'

    # Конструктор класса
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Инициализация компонента BaseSpiderComponent с требуемыми параметрами
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            # regex=r".*(([0-9]*[.,])?[0-9]{3}).*",
            path={
                'price_reg': '//*[@id="pricing-tables1-h"]/div/div/div[1]/div[1]/div/span[2]/text()',
                'price_prolong': '//*[@id="pricing-tables1-h"]/div/div/div[1]/div[1]/div/span[2]/text()',
                'price_change': '//*[@id="pricing-tables1-h"]/div/div/div[1]/div[1]/div/span[2]/text()'
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)
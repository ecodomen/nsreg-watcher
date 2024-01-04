import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregSalenamesSpider(scrapy.Spider):
    name = 'nsreg_salenames_spider'

    start_urls = ['https://www.salenames.ru/ru/page/tarify']
    allowed_domains = ['https://www.salenames.ru']
    site_names = 'ООО «СэйлНэймс»'

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
                'price_reg': '//*[@id="content"]/div/div/table[1]/tbody/tr[1]/td[2]/text()',
                'price_prolong': '//*[@id="content"]/div/div/table[1]/tbody/tr[2]/td[2]/text()',
                'price_change': '//*[@id="content"]/div/div/table[1]/tbody/tr[3]/td[2]/text()'
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

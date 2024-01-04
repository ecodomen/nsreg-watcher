import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregUninicSpider(scrapy.Spider):
    name = 'nsreg_uninic_spider'

    start_urls = ['https://uninic.ru/domainreg.php']
    allowed_domains = 'https://uninic.ru/'
    site_names = 'ООО «Объединенные доменные имена»'

    # Конструктор класса
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Инициализация компонента BaseSpiderComponent с требуемыми параметрами
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9]+[.,\s])?руб",
            path={
                'price_reg': '/html/body/div[1]/div/div[2]/div[1]/div/div/div[3]/table/tr[2]/td[3]/b[1]/text()',
                'price_prolong': '/html/body/div[1]/div/div[2]/div[1]/div/div/div[3]/table/tr[2]/td[5]/b[1]/text()',
                'price_change': None
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

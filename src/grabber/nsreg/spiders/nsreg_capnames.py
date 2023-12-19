import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregCapnamesSpider(scrapy.Spider):
    name = "nsreg_capnames.py"
    start_urls = ["https://domainshop.ru/services/"]
    allowed_domains = ("https://capnames.ru/")
    site_names = ("ООО «КАПИТАЛЪ»",)

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
                'price_reg': '//*[@id="overlappable-2"]/div/div/div/div[1]/div/div/div[2]/div/p[1]/text()',
                'price_prolong': '//*[@id="overlappable-2"]/div/div/div/div[2]/div/div/div[2]/div/p[1]/text()',
                'price_change': '//*[@id="overlappable-2"]/div/div/div/div[3]/div/div/div[2]/div/p[1]/text()'
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)
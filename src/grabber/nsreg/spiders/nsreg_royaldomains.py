import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregRoyaldomainsSpider(scrapy.Spider):
    name = 'nsreg_royaldomains_spider'

    start_urls = ['https://royaldomains.ru//']
    allowed_domains = ['https://royaldomains.ru/']
    site_names = ('ООО «РОЯЛЬ»',)

    # Конструктор класса
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Инициализация компонента BaseSpiderComponent с требуемыми параметрами
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9]{1,3}(?:\s[0-9]{3})*\s?)?₽",
            path={
                'price_reg': '//*[@id="about"]/div/div/figure/table/tbody/tr[1]/td[3]',
                'price_prolong': '//*[@id="about"]/div/div/figure/table/tbody/tr[2]/td[3]',
                'price_change': '//*[@id="about"]/div/div/figure/table/tbody/tr[3]/td[3]'
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

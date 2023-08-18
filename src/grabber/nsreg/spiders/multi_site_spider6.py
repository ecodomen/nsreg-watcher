"""
Наименования сайтов: ООО «Клеверег», ООО «Таргетнэймс», ООО «Технэймс»

Адреса сайтов: https://clevereg.ru, https://targetnames.ru, https://technames.ru

"""


import scrapy

from ..base_site_spider import BaseSpiderComponent


class MultiSiteSpider6(scrapy.Spider):
    name = 'multi_site_spider6'

    start_urls = (
        'https://clevereg.ru/tariffs/',
        'https://targetnames.ru/tariffs/',
        'https://technames.ru/tariffs/'
    )
    allowed_domains = (
        'https://clevereg.ru',
        'https://targetnames.ru',
        'https://technames.ru'
    )
    site_names = (
        'ООО «Клеверег»',
        'ООО «Таргетнэймс»',
        'ООО «Технэймс»'
    )

    # Конструктор класса
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Инициализация компонента BaseSpiderComponent с требуемыми параметрами
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9]{1,3}(?:\s[0-9]{3})*[.,\s]?)?руб\.",
            path={
                'price_reg': '//*[@id="post-66"]/div/div/figure/table/tbody/tr[1]/td[2]',
                'price_prolong': '//*[@id="post-66"]/div/div/figure/table/tbody/tr[2]/td[2]',
                'price_change': '//*[@id="post-66"]/div/div/figure/table/tbody/tr[3]/td[2]'
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)
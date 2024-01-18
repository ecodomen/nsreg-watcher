"""
Наименования сайтов: ООО «БИТНЭЙМС», ООО «Бэтнеймс», ООО «Пар», ООО «РЕГЕОН», ООО «Регион»,
 ООО «СМП №2»

Адреса сайтов: https://bitnames.ru, https://betnames.ru, https://parpro.ru,
http://regeon.ru, https://regiondomains.ru, https://tapereg.ru,

"""

import scrapy

from ..base_site_spider import BaseSpiderComponent


class MultiSiteSpider3(scrapy.Spider):
    name = 'multi_site_spider3'

    start_urls = (
        'https://bitnames.ru/#features-2',
        'https://betnames.ru/#features-2',
        'https://parpro.ru/#features-2',
        'http://regeon.ru/#features-2',
        'https://regiondomains.ru/#features-2',
        'https://tapereg.ru/#features-2'
    )
    allowed_domains = (
        'bitnames.ru',
        'betnames.ru',
        'parpro.ru',
        'regeon.ru',
        'regiondomains.ru',
        'tapereg.ru'
    )
    site_names = (
        'ООО «БИТНЭЙМС»',
        'ООО «Бэтнеймс»',
        'ООО «Пар»',
        'ООО «РЕГЕОН»',
        'ООО «Регион»',
        'ООО «СМП №2»'
    )

    # Конструктор класса
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Инициализация компонента BaseSpiderComponent с требуемыми параметрами
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r".*?(\d+).*",
            path={
                'price_reg': (
                    'translate(/html/body/div[2]/div[2]/div/div[1]/div/div/div[1]/div/p/text(), " ", "")'
                ),
                'price_prolong': (
                    'translate(/html/body/div[2]/div[2]/div/div[1]/div/div/div[2]/div/p/text(), " ", "")'
                ),
                'price_change': (
                    'translate(/html/body/div[2]/div[2]/div/div[1]/div/div/div[3]/div/p/text(), " ", "")'
                )
            }

        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

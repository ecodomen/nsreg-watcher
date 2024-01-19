"""
Наименования сайтов: ООО «ДНС», ООО «ИТ», ООО «КЛАСТЕР», ООО «КОД», ООО «Мега», ООО «Облако»,
ООО «ПОЧТА», ООО «ПРО», ООО «ПРОКСИ»

Адреса сайтов: https://fastdns.ru, https://4it.ru, https://clustered.ru, https://thecode.ru, http://megahost.ru,
https://cloudy.ru,https://startmail.ru,https://proprovider.ru,https://dproxy.ru,

"""

import scrapy

from ..base_site_spider import BaseSpiderComponent


class MultiSiteSpider4(scrapy.Spider):
    name = 'multi_site_spider4'

    start_urls = (
        'https://fastdns.ru/#price',
        'https://4it.ru/#price',
        'https://clustered.ru/#price',
        'https://thecode.ru/#price',
        'http://megahost.ru/#price',
        'https://cloudy.ru/#price',
        'https://startmail.ru/#price',
        'https://proprovider.ru/#price',
        'https://dproxy.ru/#price'
    )
    allowed_domains = (
        'fastdns.ru',
        '4it.ru',
        'clustered.ru',
        'thecode.ru',
        'megahost.ru',
        'cloudy.ru',
        'startmail.ru',
        'proprovider.ru',
        'dproxy.ru'
    )
    site_names = (
        'ООО «ДНС»',
        'ООО «ИТ»',
        'ООО «КЛАСТЕР»',
        'ООО «КОД»',
        'ООО «Мега»',
        'ООО «Облако»',
        'ООО «ПОЧТА»',
        'ООО «ПРО»',
        'ООО «ПРОКСИ»'
    )

    # Конструктор класса
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Инициализация компонента BaseSpiderComponent с требуемыми параметрами
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9]+)\s+₽.*",
            path={
                'price_reg': (
                    '/html/body/main/section[4]/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]/div/table/tbody/tr[2]/td[2]/div/p/text()'
                ),
                'price_prolong': (
                    '/html/body/main/section[4]/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]/div/table/tbody/tr[3]/td[2]/div/p/text()'
                ),
                'price_change': (
                    '/html/body/main/section[4]/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]/div/table/tbody/tr[4]/td[2]/div/p/text()'
                )
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

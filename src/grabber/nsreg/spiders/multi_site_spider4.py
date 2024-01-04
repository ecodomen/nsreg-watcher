"""
Наименования сайтов: ООО «ДНС», ООО «ИТ», ООО «КЛАСТЕР», ООО «КОД», ООО «Мега», ООО «НФ МЕДИА», ООО «Облако»,
ООО «Открытые коммуникации», ООО «ПОЧТА», ООО «ПРО», ООО «ПРОКСИ»

Адреса сайтов: https://fastdns.ru, https://4it.ru, https://clustered.ru, https://thecode.ru, http://megahost.ru,
http://openreg.ru,https://cloudy.ru,https://opencom.ru,https://startmail.ru,https://proprovider.ru,https://dproxy.ru,

ООО «НФ МЕДИА» и  ООО «Открытые коммуникации» закомментированы, т.к. есть подозрение, что они не подходят под данную
группу

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
        # 'http://openreg.ru/#price',
        'https://cloudy.ru/#price',
        # 'https://opencom.ru/#price',
        'https://startmail.ru/#price',
        'https://proprovider.ru/#price',
        'https://dproxy.ru/#price'
    )
    allowed_domains = (
        'https://fastdns.ru',
        'https://4it.ru',
        'https://clustered.ru',
        'https://thecode.ru',
        'http://megahost.ru',
        # 'http://openreg.ru',
        'https://cloudy.ru',
        # 'https://opencom.ru',
        'https://startmail.ru',
        'https://proprovider.ru',
        'https://dproxy.ru'
    ),
    site_names = (
        'ООО «ДНС»',
        'ООО «ИТ»',
        'ООО «КЛАСТЕР»',
        'ООО «КОД»',
        'ООО «Мега»',
        # 'ООО «НФ МЕДИА»',
        'ООО «Облако»',
        # 'ООО «Открытые коммуникации»',
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
                    '/html/body/div[1]/div[4]/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]/div/'
                    'table/tbody/tr[2]/td[2]/div/p/text()'
                ),
                'price_prolong': (
                    '/html/body/div[1]/div[4]/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]/div/'
                    'table/tbody/tr[3]/td[2]/div/p/text()'
                ),
                'price_change': (
                    '/html/body/div[1]/div[4]/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]/div/'
                    'table/tbody/tr[4]/td[2]/div/p/text()'
                )
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

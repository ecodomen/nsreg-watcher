"""
Наименования сайтов: ООО «Актив.Домэинс», ООО «Ардис», ООО «Домэинреселлер», ООО «Домэинс24», ООО «Приватнэймс»,
ООО «РУ-ДОМЭИНС»

Адреса сайтов: http://active.domains, https://ardis.ru, https://domainreseller.ru, https://domains24.ru,
http://private-names.ru,https://ru-domains.ru,

"""

import scrapy

from ..base_site_spider import BaseSpiderComponent


class MultiSiteSpider5(scrapy.Spider):
    name = 'multi_site_spider5'
    start_urls = (
                'https://active.domains/domains/',
                'https://ardis.ru/domains/',
                'https://domainreseller.ru/domains/',
                'https://domains24.ru/domains/',
                'https://private-names.ru/domains/',
                'https://ru-domains.ru/domains/',
    )
    allowed_domains = (
                'https://active.domains',
                'https://ardis.ru',
                'https://domainreseller.ru',
                'https://domains24.ru',
                'http://private-names.ru',
                'https://ru-domains.ru',
    )
    site_names = (
                'ООО «Актив.Домэинс»',
                'ООО «Ардис»',
                'ООО «Домэинреселлер»',
                'ООО «Домэинс24»',
                'ООО «Приватнэймс»',
                'ООО «РУ-ДОМЭИНС»',
    )

    # Конструктор класса
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Инициализация компонента BaseSpiderComponent с требуемыми параметрами
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r".*(([0-9]*[.,])?[0-9]{3}).*",
            path={
                'price_reg': '//*[@id="show_domain"]/div/div/table/tbody/tr[1]/td[3]/a/text()',
                'price_prolong': '//*[@id="show_domain"]/div/div/table/tbody/tr[1]/td[4]/a/text()',
                'price_change': '//*[@id="show_domain"]/div/div/table/tbody/tr[1]/td[5]/a/text()'
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

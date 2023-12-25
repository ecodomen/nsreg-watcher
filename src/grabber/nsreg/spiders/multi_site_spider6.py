"""
Наименования сайтов: ООО «Клеверег», ООО «Таргетнэймс», ООО «Технэймс»

Адреса сайтов: https://clevereg.ru, https://targetnames.ru, https://technames.ru

"""


import scrapy

from ..base_site_spider import BaseSpiderComponent
from ..utils import find_price_sub
from nsreg.items import NsregItem

EMPTY_PRICE = {
    'price_reg': None,
    'price_prolong': None,
    'price_change': None,
}

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
                'price_reg': '//*[@id="post-66"]/div/div/figure/table/tbody/tr[1]/td[2]/text()',
                'price_prolong': '//*[@id="post-66"]/div/div/figure/table/tbody/tr[2]/td[2]/text()',
                'price_change': '//*[@id="post-66"]/div/div/figure/table/tbody/tr[3]/td[2]/text()'
            }
        )

    # Parse с использованием функции find_price_sub
    def parse(self, response):
        price_reg = response.xpath(self.component.path['price_reg']).get()
        price_reg = find_price_sub(self.component.regex['price_reg'], price_reg)

        price_prolong = response.xpath(self.component.path['price_prolong']).get()
        price_prolong = find_price_sub(self.component.regex['price_prolong'], price_prolong)

        price_change = response.xpath(self.component.path['price_change']).get()
        price_change = find_price_sub(self.component.regex['price_change'], price_change)

        item = NsregItem()
        item['name'] = self.site_names[self.start_urls.index(response.url)]
        price = item.get('price', EMPTY_PRICE)
        price['price_change'] = price_change
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        item['price'] = price

        return item
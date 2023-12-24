import logging
import re
import scrapy

from .items import NsregItem

# Класс, реализующий основные компоненты паука для веб-скрапинга
class AbstractSpiderComponent(scrapy.Spider):
    start_urls = None
    allowed_domains = None
    site_names = None
    regex = None
    path = None
    EMPTY_PRICE = {
        'price_reg': None,
        'price_prolong': None,
        'price_change': None,
    }
    # шаг парсинга, если несколько сайтов
    parse_step = -1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not isinstance(self.regex, dict):
            self.regex = {
                'price_reg': self.regex,
                'price_prolong': self.regex,
                'price_change': self.regex
            }

    # Функция поиска цен в тексте, используя регулярное выражение
    def find_price(self, re_pattern, price):
        price = str(price).strip()
        if price.casefold() == "бесплатно":
            price = 0
        else:
            # Применяем регулярное выражение к строке
            if m := re.match(re_pattern, price):
                price = m.group(1)
        price = f'{float(price)}'
        logging.info('price = %s', price)

        return price

    """ Функция для обработки полученных данных """
    def parse(self, response):
        self.parse_step += 1
        # Получение имя сайта
        item = NsregItem()
        item['name'] = self.site_names[self.parse_step]
        item['price'] = self.EMPTY_PRICE

        return self.parse_price_reg(response, item)

    """ Поиск цены на регистрацию домена на веб-странице """
    def parse_price_reg(self, response, item):
        price_reg = response.xpath(self.path['price_reg']).get()
        price_reg = self.find_price(self.regex['price_reg'], price_reg)
        item['price']['price_reg'] = price_reg

        return self.parse_price_prolong(response, item)

    """ Поиск цены на продление домена на веб-странице """
    def parse_price_prolong(self, response, item):
        price_prolong = response.xpath(self.path['price_prolong']).get()
        price_prolong = self.find_price(self.regex['price_prolong'], price_prolong)
        item['price']['price_prolong'] = price_prolong

        return self.parse_price_change(response, item)

    """ Поиск цены на изменение|перенос домена на веб-странице """
    def parse_price_change(self, response, item):
        price_change = response.xpath(self.path['price_change']).get()
        price_change = self.find_price(self.regex['price_change'], price_change)
        item['price']['price_change'] = price_change

        yield item
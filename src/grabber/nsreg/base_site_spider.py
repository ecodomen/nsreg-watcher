import logging
import re

from .items import NsregItem

PRICE_DEFAULT_DICT = {
    'price_reg': None,
    'price_prolong': None,
    'price_change': None,
}

PRICE_FREE_PATTERNS = (
    "бесплатно", "перенос в подарок",
)


def find_price(re_pattern, price):
    """Функция поиска цен в тексте, используя регулярное выражение"""
    price = str(price).strip()
    if price in PRICE_FREE_PATTERNS:
        price = 0
    else:
        # Применяем регулярное выражение к строке
        if m := re.match(re_pattern, price):
            price = m.group(1)
    price = f'{float(price)}'
    logging.info('price = %s', price)

    return price


class BaseSpiderComponent:
    """Класс, реализующий основные компоненты паука для веб-скрапинга"""

    def __init__(self, start_urls=None, allowed_domains=None, site_names=None, regex=None, path=None):
        # Разделение строк по запятым и преобразуем их в списки
        self.start_urls = start_urls
        self.allowed_domains = allowed_domains
        self.site_names = site_names
        # Сохранение регулярных выражений и пути xpath для дальнейшего использования
        # В качестве регулярных выражений принимается либо str, либо dict с полями price_reg, price_prolong и price_change
        # regex-строка преобразуется в dict с одинаковыми значениями в полях
        if not isinstance(regex, dict):
            regex = {
                'price_reg': regex,
                'price_prolong': regex,
                'price_change': regex
            }
        self.regex = regex
        self.path = path

    def parse(self, response):
        """Функция для обработки полученных данных"""

        # Поиск цены на регистрацию домена на веб-странице
        price_reg = response.xpath(self.path['price_reg']).get()
        price_reg = find_price(self.regex['price_reg'], price_reg)

        # Поиск цены на продление домена на веб-странице
        price_prolong = response.xpath(self.path['price_prolong']).get()
        price_prolong = find_price(self.regex['price_prolong'], price_prolong)

        # Поиск цены на изменение домена на веб-странице
        price_change = response.xpath(self.path['price_change']).get()
        price_change = find_price(self.regex['price_change'], price_change)

        # Получение имя сайта
        site_name = self.site_names[self.start_urls.index(response.url)]

        # Создание элемента данных и заполнение его информацией
        item = NsregItem()
        item['name'] = site_name
        price = item.get('price', PRICE_DEFAULT_DICT)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        price['price_change'] = price_change
        item['price'] = price

        return item

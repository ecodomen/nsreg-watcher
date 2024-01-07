import logging
import re
from urllib.parse import urlparse

from .items import NsregItem

EMPTY_PRICE = {
    'price_reg': None,
    'price_prolong': None,
    'price_change': None,
}


# Функция поиска цен в тексте, используя регулярное выражение
def find_price(re_pattern, price):
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


# Класс, реализующий основные компоненты паука для веб-скрапинга
class BaseSpiderComponent:

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

    # Функция для обработки полученных данных
    def parse(self, response):
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
        start_urls_netloc = [urlparse(url).netloc for url in self.start_urls]
        response_url_netloc = urlparse(response.url).netloc
        site_name = self.site_names[start_urls_netloc.index(response_url_netloc)]

        # Создание элемента данных и заполнение его информацией
        item = NsregItem()
        item['name'] = site_name
        price = item.get('price', EMPTY_PRICE)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        price['price_change'] = price_change
        item['price'] = price

        return item

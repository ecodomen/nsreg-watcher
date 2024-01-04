# -*- coding: utf-8 -*-
# УДАЛИТЬ ПОСЛЕ РЕФАКТОРА СПАЙДЕРОВ
from nsreg.items import NsregItem

from nsreg.utils import find_price


EMPTY_PRICE = {
    'price_reg': None,
    'price_prolong': None,
    'price_change': None,
}


# Example site
# https://www.powerhosting.ru/site/tariffs
def moscow_tariffs(self, response, re_pattern, name):
    price_reg = response.xpath(
        '/html/body/section/div/div/div/div[2]/div[1]/div[2]/span/text()').get()
    price_reg = find_price(re_pattern, price_reg)

    price_prolong = response.xpath(
        '/html/body/section/div/div/div/div[2]/div[2]/div[2]/span/text()').get()
    price_prolong = find_price(re_pattern, price_prolong)

    price_change = response.xpath(
        '/html/body/section/div/div/div/div[2]/div[3]/div[2]/span/text()').get()
    price_change = find_price(re_pattern, price_change)

    item = NsregItem()
    item['name'] = name
    price = item.get('price', EMPTY_PRICE)
    price['price_reg'] = price_reg
    price['price_prolong'] = price_prolong
    price['price_change'] = price_change
    item['price'] = price

    return item


# Example site
# https://www.clickhost24.ru/price/
def moscow_price(self, response, re_pattern, name):
    price_reg = response.xpath(
        '/html/body/div[1]/div[3]/article/section/table[1]/tr/td[1]/article[1]/div/table/tr[5]/td[2]/text()').get()
    price_reg = find_price(re_pattern, price_reg)

    price_prolong = response.xpath(
        '/html/body/div[1]/div[3]/article/section/table[1]/tr/td[1]/article[1]/div/table/tr[5]/td[3]/text()').get()
    price_prolong = find_price(re_pattern, price_prolong)

    price_change = response.xpath(
        '/html/body/div[1]/div[3]/article/section/table[2]/tr/td[1]/article[2]/div/table/tr[10]/td[2]/text()').get()
    price_change = find_price(re_pattern, price_change)

    item = NsregItem()
    item['name'] = name
    price = item.get('price', EMPTY_PRICE)
    price['price_reg'] = price_reg
    price['price_prolong'] = price_prolong
    price['price_change'] = price_change
    item['price'] = price

    return item

# Exaple site
# https://clustered.ru/#price


def moscow_rich_price(self, response, re_pattern, name):
    price_reg = response.xpath(
        '/html/body/main/section[4]/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]/div/table/tbody/tr[2]/td[2]/div/p/text()').get()
    price_reg = find_price(re_pattern, price_reg)

    price_prolong = response.xpath(
        '/html/body/main/section[4]/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]/div/table/tbody/tr[3]/td[2]/div/p/text()').get()
    price_prolong = find_price(re_pattern, price_prolong)

    price_change = response.xpath(
        '/html/body/main/section[4]/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]/div/table/tbody/tr[4]/td[2]/div/p/text()').get()
    price_change = find_price(re_pattern, price_change)

    item = NsregItem()
    item['name'] = name
    price = item.get('price', EMPTY_PRICE)
    price['price_reg'] = price_reg
    price['price_prolong'] = price_prolong
    price['price_change'] = price_change
    item['price'] = price

    return item

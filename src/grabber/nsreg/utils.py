# УДАЛИТЬ ПОСЛЕ РЕФАКТОРА СПАЙДЕРОВ
import logging
import re


def find_price(re_pattern, price):
    price = str(price).strip()
    if price == "бесплатно":
        price = 0
    else:
        if m := re.match(re_pattern, price):
            price = m.group(1)
    price = f'{float(price)}'
    logging.info('price = %s', price)

    return price


def find_price_sub(re_pattern, price):
    price = str(price).strip()
    if m := re.match(re_pattern, price):
        price = m.group(1)
        price = re.sub(r'\s', '', price)
        price = f'{float(price)}'
        logging.info('price = %s', price)

        return price


def find_price_withoutre(price):
    price = str(price)
    price = re.sub(r'\s', '', price)
    price = f'{float(price)}'
    logging.info('price = %s', price)

    return price

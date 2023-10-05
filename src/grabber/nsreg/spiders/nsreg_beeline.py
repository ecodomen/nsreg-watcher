# -*- coding: utf-8 -*-
import scrapy
from nsreg.items import NsregItem

from ..utils import find_price
# работает
REGEX_PATTERN = r"([0-9]+[.,\s])?руб"
EMPTY_PRICE = {
    'price_reg': None,
    'price_prolong': None,
    'price_change': None,
}


class NsregBeelineSpider(scrapy.Spider):
    name = 'nsreg_beeline'
    allowed_domains = ['moskva.beeline.ru']
    start_urls = [
        'https://moskva.beeline.ru/business/domen/registratsiya-i-podderzhka-domenov/']

    def parse(self, response):
        price_reg = response.xpath(
            '//*[@id="react_aDGOLumF5U2Eyvb2G5m2g"]/div/div[3]/div[3]/section[1]/div/section/div[2]/div[2]/div[1]/div/div[2]/div[1]/span/text()').get()
        price_reg = find_price(REGEX_PATTERN, price_reg)

        price_prolong = response.xpath(
            '//*[@id="react_aDGOLumF5U2Eyvb2G5m2g"]/div/div[3]/div[3]/section[1]/div/section/div[2]/div[2]/div[1]/div/div[2]/div[1]/span/text()').get()
        price_prolong = find_price(REGEX_PATTERN, price_prolong)

        price_change = None

        item = NsregItem()
        item['name'] = "ПАО «ВымпелКом»"
        price = item.get('price', EMPTY_PRICE)
        price['price_reg'] = price_reg
        price['price_prolong'] = price_prolong
        price['price_change'] = price_change
        item['price'] = price

        yield item

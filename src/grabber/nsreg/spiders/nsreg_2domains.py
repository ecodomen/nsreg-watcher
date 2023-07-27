# -*- coding: utf-8 -*-
from nsreg.superspider import SuperSpider


REGEX_PROLONG_PATTERN = r".*Продление\s+—\s+(([0-9]*[.,])?[0-9]+)\s+₽.*"
REGEX_CHANGE_PATTERN = r".*(([0-9]*[.,])?[0-9]{3})\s+₽.*"
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}


class Nsreg2domainsSpider(SuperSpider):
    name = 'nsreg_2domains'
    allowed_domains = ['2domains.ru']
    start_urls = ['https://2domains.ru/domains']

    rusname = "ООО «2ДОМЕЙНС.РУ»"
    pathreg = '//*[@id="app"]/div[1]/section[3]/div/div[1]/div[1]/a/div[2]/text()'
    pathprolong = '//*[@id="app"]/div[1]/section[3]/div/div[1]/div[1]/a/div[4]/text()'
    pathchange = '/html/body/div/div[1]/section[1]/div/div/div/div/div[2]/div[2]/div/span/text()'

    regex_reg = r"\s"
    regex_prolong = r".*Продление\s+—\s+(([0-9]*[.,])?[0-9]+)\s+₽.*"
    regex_change = r".*(([0-9]*[.,])?[0-9]{3})\s+₽.*"

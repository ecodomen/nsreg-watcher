# -*- coding: utf-8 -*-
from nsreg.superspider import SuperSpider


class Nsreg4itSpider(SuperSpider):
    name = "nsreg_4it"
    allowed_domains = ["4it.ru"]
    start_urls = ["https://4it.ru/#price"]
    rusname = "ООО «ИТ»"
    pathreg = '/html/body/div[1]/div[4]/div/div[2]/div[3]/div/div/div/div[2]/div/' \
        'div/div[1]/div/table/tbody/tr[2]/td[2]/div/p/text()'
    pathprolong = '/html/body/div[1]/div[4]/div/div[2]/div[3]/div/div/div/div[2]/div/' \
        'div/div[2]/div[3]/table/tr[2]/td/div/p/text()'
    pathchange = '/html/body/div[1]/div[4]/div/div[2]/div[3]/div/div/div/div[2]/div/' \
        'div/div[2]/div[3]/table/tr[2]/td/div/p/text()'

    regex_reg = r"(([0-9]*[.,])?[0-9]*)\s+₽.*"
    regex_prolong = r"(([0-9]*[.,])?[0-9]*)\s+₽.*"
    regex_change = r"(([0-9]*[.,])?[0-9]*)\s+₽.*"

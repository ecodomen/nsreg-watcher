# -*- coding: utf-8 -*-
from nsreg.superspider import SuperSpider

import scrapy
from nsreg.items import NsregItem

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

    def parse_pricechange(self, response):
        pricechange = response.xpath(self.pathchange).get()
        pricechange = self.find_price(self.regex_change, pricechange)

        item = NsregItem()
        item['name'] = "ООО «2ДОМЕЙНС.РУ»"  
        price = item.get('price', EMPTY_PRICE)
        price['pricechange'] = pricechange 
        item['price'] = price  

        yield item  

    def parse(self, response):
        pricereg = response.xpath(self.pathreg).get()
        pricereg = self.find_price(self.regex_reg, pricereg)

        priceprolong = response.xpath(self.pathprolong).get()
        priceprolong = self.find_price(self.regex_prolong, priceprolong)


        yield scrapy.Request('https://2domains.ru/domains/transfer', callback=self.parse_pricechange)

        item = NsregItem()
        item['name'] = self.rusname
        price = item.get('price', EMPTY_PRICE)
        price['pricereg'] = pricereg
        price['priceprolong'] = priceprolong
        item['price'] = price

        yield item
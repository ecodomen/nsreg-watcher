'''
Наименования сайтов: ООО «БИТНЭЙМС», ООО «Бэтнеймс», ООО «КАПИТАЛЪ», ООО «НЕЙМБИТ», ООО «Пар», ООО «РЕГЕОН»,
ООО «Регион», ООО «РОЯЛЬ», ООО «РУДИ», ООО «СМП №2»

Адреса сайтов: https://bitnames.ru, https://betnames.ru, https://capnames.ru, https://namebit.ru, https://parpro.ru,
http://regeon.ru,https://regiondomains.ru,https://royaldomains.ru,https://rudy.ru,https://tapereg.ru,

'''

import scrapy
from ..items import NsregItem
from ..utils import find_price_sub

REGEX_PATTERN = r".*(\d+\s+\d+).*"
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}


class MultiSiteSpider3(scrapy.Spider):
    name = 'multi_site_spider3'

    def __init__(self, start_urls=None, allowed_domains=None, site_names=None, *args, **kwargs):
        super(MultiSiteSpider3, self).__init__(*args, **kwargs)
        self.start_urls = start_urls.split(',') if start_urls else []
        self.allowed_domains = allowed_domains.split(',') if allowed_domains else []
        self.site_names = site_names.split(',') if site_names else []

    def parse(self, response):
        pricereg = response.xpath(
            '/html/body/div[1]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/p[1]/text()').get()
        pricereg = find_price_sub(REGEX_PATTERN, pricereg)

        priceprolong = response.xpath(
            '/html/body/div[1]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/p[1]/text()').get()
        priceprolong = find_price_sub(REGEX_PATTERN, priceprolong)

        pricechange = response.xpath(
            '/html/body/div[1]/div[2]/div/div/div[1]/div/div/div/div[3]/div/div/div[2]/div/p[1]/text()').get()
        pricechange = find_price_sub(REGEX_PATTERN, pricechange)

        for site_name in self.site_names:
            item = NsregItem()
            item['name'] = site_name
            price = item.get('price', EMPTY_PRICE)
            price['pricereg'] = pricereg
            price['priceprolong'] = priceprolong
            price['pricechange'] = pricechange
            item['price'] = price

            yield item

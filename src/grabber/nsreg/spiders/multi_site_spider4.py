'''
Наименования сайтов: ООО «ДНС», ООО «ИТ», ООО «КЛАСТЕР», ООО «КОД», ООО «Мега», ООО «НФ МЕДИА», ООО «Облако»,
ООО «Открытые коммуникации», ООО «ПОЧТА», ООО «ПРО», ООО «ПРОКСИ»

Адреса сайтов: https://fastdns.ru, https://4it.ru, https://clustered.ru, https://thecode.ru, http://megahost.ru,
http://openreg.ru,https://cloudy.ru,https://opencom.ru,https://startmail.ru,https://proprovider.ru,https://dproxy.ru,

'''


import scrapy
from ..items import NsregItem
from ..utils import find_price, find_price_withoutre

REGEX_PATTERN = r"([0-9]+)\s+₽.*"
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}


class MultiSiteSpider4(scrapy.Spider):
    name = 'multi_site_spider4'

    def __init__(self, start_urls=None, allowed_domains=None, site_names=None, *args, **kwargs):
        super(MultiSiteSpider4, self).__init__(*args, **kwargs)
        self.start_urls = start_urls.split(',') if start_urls else []
        self.allowed_domains = allowed_domains.split(',') if allowed_domains else []
        self.site_names = site_names.split(',') if site_names else []

    def parse(self, response):
        pricereg = response.xpath(
            '/html/body/div[1]/div[4]/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]/div/table/tbody/tr[2]/td[2]/div/p/text()').get()
        pricereg = find_price(REGEX_PATTERN, pricereg)

        priceprolong = response.xpath(
            '/html/body/div[1]/div[4]/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]/div/table/tbody/tr[3]/td[2]/div/p/text()').get()
        priceprolong = find_price(REGEX_PATTERN, priceprolong)

        pricechange = response.xpath(
            '/html/body/div[1]/div[4]/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[1]/div/table/tbody/tr[4]/td[2]/div/p/text()').get()
        pricechange = find_price(REGEX_PATTERN, pricechange)

        for site_name in self.site_names:
            item = NsregItem()
            item['name'] = site_name
            price = item.get('price', EMPTY_PRICE)
            price['pricereg'] = pricereg
            price['priceprolong'] = priceprolong
            price['pricechange'] = pricechange
            item['price'] = price

            yield item

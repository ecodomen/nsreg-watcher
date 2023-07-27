'''
Наименования сайтов: ООО «Актив.Домэинс», ООО «Ардис», ООО «Домэинреселлер», ООО «Домэинс24», ООО «Приватнэймс»,
ООО «РУ-ДОМЭИНС»

Адреса сайтов: http://active.domains, https://ardis.ru, https://domainreseller.ru, https://domains24.ru,
http://private-names.ru,https://ru-domains.ru,

'''


import scrapy
from ..items import NsregItem
from ..utils import find_price

REGEX_PATTERN = r".*(([0-9]*[.,])?[0-9]{3}).*"
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}


class MultiSiteSpider5(scrapy.Spider):
    name = 'multi_site_spider5'

    def __init__(self, start_urls=None, allowed_domains=None, site_names=None, *args, **kwargs):
        super(MultiSiteSpider5, self).__init__(*args, **kwargs)
        self.start_urls = start_urls.split(',') if start_urls else []
        self.allowed_domains = allowed_domains.split(',') if allowed_domains else []
        self.site_names = site_names.split(',') if site_names else []

    def parse(self, response):
        pricereg = response.xpath('//*[@id="show_domain"]/div/div/table/tbody/tr[1]/td[3]/a/text()').get()
        pricereg = find_price(REGEX_PATTERN, pricereg)

        priceprolong = response.xpath('//*[@id="show_domain"]/div/div/table/tbody/tr[1]/td[4]/a/text()').get()
        priceprolong = find_price(REGEX_PATTERN, priceprolong)

        pricechange = response.xpath('//*[@id="show_domain"]/div/div/table/tbody/tr[1]/td[5]/a/text()').get()
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

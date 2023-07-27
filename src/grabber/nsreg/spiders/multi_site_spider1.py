'''
Наименования сайтов: ООО «101домен Регистрация Доменов», ООО «Аукцион доменов», ООО «Безопасный регистратор»,
ООО «Быстрый Хостинг», ООО «Гига Хостинг», ООО «Городские Домены», ООО «Дата Плюс», ООО «Дата Сити», ООО «Дом Доменов»,
ООО «Дом Хостинга», ООО «Доменные Сервисы», ООО «Доменный Мастер», ООО «Домены Плюс», ООО «Домены Хостинг»,
ООО «ДОМЕНЫ.РУ», ООО «Домэйн Агент», ООО «Домэйн Груп», ООО «Зона Доменов», ООО «Изи Хостинг», ООО «Магазин Доменов»
АО «Международный сетевой технический центр», ООО «Мир Доменов», ООО «Мир Хостинга», ООО «Мощный Хостинг»,
ООО «Мультирег», ООО «НэтДата», ООО «Опен Домэйнс», ООО «Приват Домэйнс», ООО «Приват Хостинг», ООО «Проф Хостинг»,
ООО «Регио», ООО «Регис», ООО «Регистр 1», ООО «Смарт Домэйнс», ООО «Техно Дата», ООО «Турбо Хостинг»,
ООО «Фабрика Доменов», ООО «ФАЕРФОКС», ООО «Хостинг Парк», ООО «Хот Хостинг», ООО «Центр Доменов», ООО «Ю.РУ»

Адреса сайтов: https://sidename.ru, https://domainauction.ru, https://www.safereg.ru, https://www.speedhosting.ru,
https://www.gigahosting.ru, https://citydomains.ru, https://www.data-plus.ru, https://www.datacity.ru,
https://domainhouse.ru, https://www.domhostinga.ru, https://domainservice.ru, https://domainmaster.ru,
https://domainplus.ru, https://www.domainshosting.ru, https://domains.ru, https://domainagent.ru,
https://domaingroup.ru, https://zonadomenov.ru, https://www.easyhosting.ru, https://domain.ru, https://mstci.ru,
https://mirdomenov.ru, https://www.mirhostinga.ru, https://www.powerhosting.ru, https://www.multireg.ru,
https://www.netdata.ru, https://opendomains.ru, https://privatedomains.ru, https://www.privatehosting.ru,
https://www.profhosting.ru, https://www.regio.ru, https://www.regis.ru, http://registr1.ru, https://smartdomains.ru,
https://www.technodata.ru, https://www.turbohosting.ru, http://domainfactory.ru, http://firefox.ru,
https://www.hostingpark.ru, https://www.hothosting.ru, http://domaincenter.ru, http://yu.ru

Пример запуска на 2 сайта: scrapy crawl nsreg_1_sites -a start_urls=https://sidename.ru/site/tariffs,
https://domainauction.ru/site/tariffs -a allowed_domains=sidename.ru,domainauction.ru -a
site_names=ООО «101домен Регистрация Доменов»,ООО «Аукцион доменов»

'''

import scrapy

from ..items import NsregItem
from ..utils import find_price


REGEX_PATTERN = r"([0-9]+[.,\s])?руб"

EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}

PRICE_XPATHS = {
    'pricereg': '/html/body/section/div/div/div/div[2]/div[1]/div[2]/span/text()',
    'priceprolong': '/html/body/section/div/div/div/div[2]/div[2]/div[2]/span/text()',
    'pricechange': '/html/body/section/div/div/div/div[2]/div[3]/div[2]/span/text()',
}

class MultiSiteSpider1(scrapy.Spider):
    name = 'multi_site_spider1'

    def __init__(self, start_urls=None, allowed_domains=None, site_names=None, *args, **kwargs):
        super(MultiSiteSpider1, self).__init__(*args, **kwargs)
        if start_urls is not None:
            self.start_urls = start_urls.split(',')
        if allowed_domains is not None:
            self.allowed_domains = allowed_domains.split(',')
        if site_names is not None:
            self.site_names = site_names.split(',')
        else:
            self.site_names = ["ООО «101домен Регистрация Доменов»"] * len(self.start_urls)

    def parse(self, response):
        item = NsregItem()
        url_index = self.start_urls.index(response.url)
        item['name'] = self.site_names[url_index]
        price = item.get('price', EMPTY_PRICE)

        for price_key, xpath in PRICE_XPATHS.items():
            price_value = response.xpath(xpath).get()
            price[price_key] = find_price(REGEX_PATTERN, price_value)

        item['price'] = price
        yield item

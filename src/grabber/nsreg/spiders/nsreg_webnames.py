import scrapy
from ..abstract_spider import AbstractSpiderComponent

class NsregWebnamesSpider(AbstractSpiderComponent):
    name = "nsreg_webnames"

    start_urls = ["https://www.webnames.ru/tld/catalog/ru", "https://webnames.ru/tld/catalog/ru"]
    allowed_domains = ("webnames.ru",)
    site_names = ("ООО «Регтайм»", "ООО «Имена Интернет»",)

    regex = {
        'price_reg': r"([0-9]+)[.,\s]?₽*",
        'price_prolong': r"([0-9]+)[.,\s]?₽*",
        'price_change': r"([0-9]+)[.,\s]?Р.*"
    }
    path = {
        'price_reg': '//*[@class="onetld__domain-info"]/table/tbody/tr[1]/td[2]/strong/text()',
        'price_prolong': '//*[@class="onetld__domain-info"]/table/tbody/tr[3]/td[2]/strong/text()',
        'price_change': '/html/body/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/span/text()'
    }

    """ Продление домена """
    def parse_price_prolong(self, response, item):
        super().parse_price_prolong(response, item)
        return scrapy.Request(
            'https://www.webnames.ru/domains/transfer/',
            callback=self.parse_price_change,
            dont_filter=True,
            cb_kwargs = dict(item = item)
        )




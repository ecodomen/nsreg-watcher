import scrapy

from ..base_site_spider import BaseSpiderComponent, EMPTY_PRICE, find_price
from ..items import NsregItem

REGEX_PATTERN = r"([0-9]+[.,\s])?руб"


class NsregRegplanetSpider(scrapy.Spider):
    name = "nsreg_regplanet"
    allowed_domains = ["regplanet.ru"]
    start_urls = ["https://www.regplanet.ru/price/"]
    site_names = ("ООО «РЕГ.РУ ДОМЕНЫ ХОСТИНГ»",)

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=REGEX_PATTERN,
            path={
                "price_reg": (
                    "/html/body/div[1]/div[3]/article/section/table[1]/tr/td[1]/article[1]/"
                    "div/table/tr[5]/td[2]/text()"
                ),
                "price_prolong": (
                    "/html/body/div[1]/div[3]/article/section/table[1]/tr/td[1]/article[1]/"
                    "div/table/tr[5]/td[3]/text()"
                ),
                "price_change": (
                    "substring("
                    "/html/body/div[1]/div[3]/div[4]/article[3]/div[2]/div/p[11]/text(), "
                    "101, 10)"
                ),
            },
        )

    def parse_price_change(self, response):
        price_change = response.xpath(self.component.path["price_change"]).get()
        price_change = find_price(self.component.regex["price_change"], price_change)

        item = NsregItem()
        item["name"] = "ООО «РЕГ.РУ ДОМЕНЫ ХОСТИНГ»"
        price = item.get("price", EMPTY_PRICE)
        price["price_change"] = price_change
        item["price"] = price

        yield item

    def parse(self, response):
        price_reg = response.xpath(self.component.path["price_reg"]).get()
        price_reg = find_price(self.component.regex["price_reg"], price_reg)

        price_prolong = response.xpath(self.component.path["price_prolong"]).get()
        price_prolong = find_price(self.component.regex["price_prolong"], price_prolong)

        yield scrapy.Request(
            "https://www.regplanet.ru/domains_faq/", callback=self.parse_price_change
        )

        item = NsregItem()
        item["name"] = "ООО «РЕГ.РУ ДОМЕНЫ ХОСТИНГ»"
        price = item.get("price", EMPTY_PRICE)
        price["price_reg"] = price_reg
        price["price_prolong"] = price_prolong
        item["price"] = price

        return item

import scrapy


from ..utils_spider import moscow_tariffs


REGEX_PATTERN = r"([0-9]+[.,\s])?руб"
name = "ООО «Приват Домэйнс»"


class NsregPrivatedomainsSpider(scrapy.Spider):
    name = "nsreg_privatedomains"
    allowed_domains = ["privatedomains.ru"]
    start_urls = ["https://privatedomains.ru/site/tariffs"]

    def parse(self, response):
        item = moscow_tariffs(self, response, REGEX_PATTERN, name)
        yield item

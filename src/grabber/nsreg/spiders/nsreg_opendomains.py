import scrapy


from ..utils_spider import moscow_tariffs


REGEX_PATTERN = r"([0-9]+[.,\s])?руб"
name = "ООО «Опен Домэйнс»"


class NsregOpendomainsSpider(scrapy.Spider):
    name = "nsreg_opendomains"
    allowed_domains = ["opendomains.ru"]
    start_urls = ["https://opendomains.ru/site/tariffs"]

    def parse(self, response):
        item = moscow_tariffs(self, response, REGEX_PATTERN, name)
        yield item

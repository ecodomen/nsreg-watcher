import scrapy

from ..utils_spider import moscow_rich_price


REGEX_PATTERN = r"([0-9]+)\s+₽.*"
name = "ООО «КОД»"


class NsregThecodeSpider(scrapy.Spider):
    name = "nsreg_thecode"
    allowed_domains = ["thecode.ru"]
    start_urls = ["https://thecode.ru/#price"]

    def parse(self, response):
        item = moscow_rich_price(self, response, REGEX_PATTERN, name)
        yield item

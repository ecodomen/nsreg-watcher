import scrapy

from ..utils_spider import moscow_rich_price


REGEX_PATTERN = r"([0-9]+)\s+₽.*"
name = "ООО «ПОЧТА»"


class NsregStartmailSpider(scrapy.Spider):
    name = "nsreg_startmail"
    allowed_domains = ["startmail.ru"]
    start_urls = ["https://startmail.ru/#price"]

    def parse(self, response):
        item = moscow_rich_price(self, response, REGEX_PATTERN, name)
        yield item

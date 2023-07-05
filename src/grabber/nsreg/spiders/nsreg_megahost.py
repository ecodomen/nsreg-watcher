import scrapy

from ..utils_spider import moscow_rich_price


REGEX_PATTERN = r"([0-9]+)\s+₽.*"
name = "ООО «Мега»"


class NsregMegahostSpider(scrapy.Spider):
    name = 'nsreg_megahost'
    allowed_domains = ['megahost.ru']
    start_urls = ['http://megahost.ru/']

    def parse(self, response):
        item = moscow_rich_price(self, response, REGEX_PATTERN, name)
        yield item

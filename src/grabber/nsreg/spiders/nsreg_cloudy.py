import scrapy

from ..utils_spider import moscow_rich_price


REGEX_PATTERN = r"([0-9]+)\s+₽.*"
name = "ООО «Облако»"



class NsregCloudySpider(scrapy.Spider):
    name = 'nsreg_cloudy'
    allowed_domains = ['cloudy.ru']
    start_urls = ['https://cloudy.ru/#price']

    def parse(self, response):
        item = moscow_rich_price(self, response, REGEX_PATTERN, name)
        yield item

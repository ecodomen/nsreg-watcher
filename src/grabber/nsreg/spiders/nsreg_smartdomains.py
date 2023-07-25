import scrapy

from ..utils_spider import moscow_tariffs


REGEX_PATTERN = r"([0-9]+[.,\s])?руб"
name = "ООО «Смарт Домэйнс»"


class NsregSmartdomainsSpider(scrapy.Spider):
    name = 'nsreg_smartdomains'
    allowed_domains = ['smartdomains.ru']
    start_urls = ['https://smartdomains.ru/site/tariffs']

    def parse(self, response):
        item = moscow_tariffs(self, response, REGEX_PATTERN, name)
        yield item

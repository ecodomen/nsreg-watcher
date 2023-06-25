import scrapy

from ..utils_spider import moscow_tariffs


REGEX_PATTERN = r"([0-9]+[.,\s])?руб"
name = "ООО «Мультирег»"


class NsregMultieregSpider(scrapy.Spider):
    name = 'nsreg_multiereg'
    allowed_domains = ['www.multireg.ru']
    start_urls = ['https://www.multireg.ru/site/tariffs']

    def parse(self, response):
        item = moscow_tariffs(self, response, REGEX_PATTERN, name)
        yield item


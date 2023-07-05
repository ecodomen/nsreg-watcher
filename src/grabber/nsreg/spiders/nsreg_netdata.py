import scrapy

from ..utils_spider import moscow_tariffs


REGEX_PATTERN = r"([0-9]+[.,\s])?руб"
name = "ООО «НэтДата»"


class NsregNetdataSpider(scrapy.Spider):
    name = 'nsreg_netdata'
    allowed_domains = ['www.netdata.ru']
    start_urls = ['https://www.netdata.ru/site/tariffs']

    def parse(self, response):
        item = moscow_tariffs(self, response, REGEX_PATTERN, name)
        yield item

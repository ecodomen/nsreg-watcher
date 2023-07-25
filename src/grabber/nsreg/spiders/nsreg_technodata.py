import scrapy

from ..utils_spider import moscow_tariffs


REGEX_PATTERN = r"([0-9]+[.,\s])?руб"
name = "ООО «Техно Дата»"


class NsregTechnodataSpider(scrapy.Spider):
    name = 'nsreg_technodata'
    allowed_domains = ['www.technodata.ru']
    start_urls = ['https://www.technodata.ru/site/tariffs']

    def parse(self, response):
        item = moscow_tariffs(self, response, REGEX_PATTERN, name)
        yield item

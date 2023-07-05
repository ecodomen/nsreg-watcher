import scrapy

from ..utils_spider import moscow_tariffs


REGEX_PATTERN = r"([0-9]+[.,\s])?руб"
name = "ООО «Мир Хостинга»"


class NsregMirhostingaSpider(scrapy.Spider):
    name = 'nsreg_mirhostinga'
    allowed_domains = ['www.mirhostinga.ru']
    start_urls = ['https://www.mirhostinga.ru/site/tariffs']

    def parse(self, response):
        item = moscow_tariffs(self, response, REGEX_PATTERN, name)
        yield item

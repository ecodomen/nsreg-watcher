import scrapy

from ..utils_spider import moscow_rich_price


REGEX_PATTERN = r"([0-9]+)\s+₽.*"
name = "ООО «КЛАСТЕР»"


class NsregClusteredSpider(scrapy.Spider):
    name = "nsreg_clustered"
    allowed_domains = ["clustered.ru"]
    start_urls = ["https://clustered.ru/#price"]

    def parse(self, response):
        item = moscow_rich_price(self, response, REGEX_PATTERN, name)
        yield item

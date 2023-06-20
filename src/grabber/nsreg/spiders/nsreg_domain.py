import scrapy

from ..utils_spider import moscow_tariffs


REGEX_PATTERN = r"([0-9]+[.,\s])?руб"
name = "ООО «Магазин Доменов»"


class NsregDomainSpider(scrapy.Spider):
    name = "nsreg_domain"
    allowed_domains = ["domain.ru"]
    start_urls = ["https://domain.ru/site/tariffs"]

    def parse(self, response):
        item = moscow_tariffs(self, response, REGEX_PATTERN, name)
        yield item

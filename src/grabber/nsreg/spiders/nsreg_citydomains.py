import scrapy


from ..utils_spider import moscow_tariffs


REGEX_PATTERN = r"([0-9]+[.,\s])?руб"
name = "ООО «Городские Домены»"


class NsregCitydomainsSpider(scrapy.Spider):
    name = "nsreg_citydomains"
    allowed_domains = ["citydomains.ru"]
    start_urls = ["https://citydomains.ru/site/tariffs"]

    def parse(self, response):
        item = moscow_tariffs(self, response, REGEX_PATTERN, name)
        yield item

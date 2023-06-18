import scrapy


from ..utils_spider import moscow_price


REGEX_PATTERN = r"([0-9]+[.,\s])?руб"
name = "ООО «КЛИКХОСТ»"


class NsregClickhostSpider(scrapy.Spider):
    name = "nsreg_clickhost"
    allowed_domains = ["www.clickhost24.ru"]
    start_urls = ["https://www.clickhost24.ru/price/"]

    def parse(self, response):
        item = moscow_price(self, response, REGEX_PATTERN, name)
        yield item

import scrapy


from ..utils_spider import moscow_price


REGEX_PATTERN = r"([0-9]+[.,\s])?руб"
name = "ООО «РЕНТЕР.РУ»"


class NsregStepmediaSpider(scrapy.Spider):
    name = 'nsreg_stepmedia'
    allowed_domains = ['www.sm-domains.ru']
    start_urls = ['https://www.sm-domains.ru/price/']

    def parse(self, response):
        item = moscow_price(self, response, REGEX_PATTERN, name)
        yield item

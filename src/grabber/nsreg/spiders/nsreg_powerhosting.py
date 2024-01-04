import scrapy


from ..utils_spider import moscow_tariffs


REGEX_PATTERN = r"([0-9]+[.,\s])?руб"
name = "ООО «Мощный Хостинг»"
# MarieCurie


class NsregPowerhostingSpider(scrapy.Spider):
    name = 'nsreg_powerhosting'
    allowed_domains = ['www.powerhosting.ru']
    start_urls = ['http://www.powerhosting.ru/site/tariffs']

    def parse(self, response):
        item = moscow_tariffs(self, response, REGEX_PATTERN, name)
        yield item

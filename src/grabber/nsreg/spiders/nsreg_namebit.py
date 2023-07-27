from collections import namedtuple
import scrapy

from ..utils_spider import parser_re
from ..utils import find_price_sub


Parser = namedtuple('Parser',  ['response', 're_pattern', 'find_func', 'name', 'pricereg', 'priceprolong', 'pricechange'])
re_pattern = r".*(\d+\s+\d+).*"
name = "ООО «НЕЙМБИТ»"
pricereg = '//*[@id="overlappable"]/div/div/div/div[1]/div/div/div[2]/div/p[1]'
priceprolong = '//*[@id="overlappable"]/div/div/div/div[2]/div/div/div[2]/div/p[1]'
pricechange = '//*[@id="overlappable"]/div/div/div/div[3]/div/div/div[2]/div/p[1]'
find_func = find_price_sub


class NsregNamebitSpider(scrapy.Spider):
    name = 'nsreg_namebit'
    allowed_domains = ['namebit.ru']
    start_urls = ['http://namebit.ru/#overlappable']

    def parse(self, response):
        parser = Parser(response, re_pattern, find_func, name, pricereg, priceprolong, pricechange)
        item = parser_re(parser)
        yield item

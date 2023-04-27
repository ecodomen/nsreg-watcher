import scrapy
from nsreg.items import NsregItem

class NSRegSpider(scrapy.Spider):
    name = "nsreg"
    start_urls = [
        'https://cctld.ru/domains/reg/',
    ]

    def parse(self, response):
        for reg in response.xpath('//*[@id="registrator-list"]/div/div'):
            item = NsregItem()
            item['name'] = reg.xpath('div/span[1]/span[1]/span/text()').get()
            item['note1'] = reg.xpath('div/span[1]/span[2]/span[1]/text()').get()
            item['note2'] = reg.xpath('div/span[1]/span[2]/span[2]/text()').get()
            item['city'] = reg.xpath('div/span[2]/text()').get()
            item['website'] = reg.xpath('div/a/@href').get()

            yield item

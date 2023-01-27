import scrapy


class NSRegSpider(scrapy.Spider):
    name = "nsreg"
    start_urls = [
        'https://cctld.ru/domains/reg/',
    ]

    def parse(self, response):
        for reg in response.xpath('//*[@id="registrator-list"]/div/div'):
            yield {
                # div/span[1]/span[1]/span
                'name': reg.xpath('div/span[1]/span[1]/span/text()').get(),
                'note1': reg.xpath('div/span[1]/span[2]/span[1]/text()').get(),
                'note2': reg.xpath('div/span[1]/span[2]/span[2]/text()').get(),
                'city': reg.xpath('div/span[2]/text()').get(),
                'website': reg.xpath('div/a/@href').get(),
                
            }

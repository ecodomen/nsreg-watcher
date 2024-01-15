import scrapy

from ..base_site_spider import BaseSpiderComponent


class MultiSiteSpider3(scrapy.Spider):
    name = 'nsreg_regdomainhost'

    start_urls = ('https://www.regdomainhost.ru/price',)
    allowed_domains = ('www.regdomainhost.ru',)
    site_names = ('ООО «ДОМЕНХОСТ»',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9]+)?руб",
            path={ 
                'price_reg':        (
                    'translate(/html/body/div[1]/div[3]/article/section/table[1]/tr/td[1]/article[1]/'
                    'div/table/tr[5]/td[2]/text(), "\xa0 ", "")'
                ),
                'price_prolong': (
                    'translate(/html/body/div[1]/div[3]/article/section/table[1]/tr/td[1]/article[1]/'
                    'div/table/tr[5]/td[3]/text(), "\xa0 ", "")'
                ),
                'price_change': (
                    'translate(/html/body/div[1]/div[3]/article/section/table[2]/tr/td[1]/article[2]/'
                    'div/table/tr[10]/td[2]/text(), "\xa0 ", "")'
                )}
        )

    def parse(self, response):
        return self.component.parse(response)

import scrapy

from ..base_site_spider import BaseSpiderComponent


class MultiSiteSpider3(scrapy.Spider):
    name = 'nsreg_rudy'

    start_urls = ('https://rudy.ru/',)
    allowed_domains = ('rudy.ru',)
    site_names = ('ООО «РУДИ»',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r".*?(\d+).*",
            path={
                'price_reg':        'translate(/html/body/div[1]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/p[1]/text(), " ", "")',
                'price_prolong':    'translate(/html/body/div[1]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/p[1]/text(), " ", "")',
                'price_change':     'translate(/html/body/div[1]/div[2]/div/div/div[1]/div/div/div/div[3]/div/div/div[2]/div/p[1]/text(), " ", "")'
            }
        )

    def parse(self, response):
        return self.component.parse(response)

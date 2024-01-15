import scrapy

from ..base_site_spider import BaseSpiderComponent


class MultiSiteSpider4(scrapy.Spider):
    name = 'nsreg_openreg'
    start_urls = ('http://openreg.ru/',)
    allowed_domains = ('openreg.ru',)
    site_names = ('ООО «НФ МЕДИА»',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9]+)₽.*",
            path={
                'price_reg': 'translate(/html/body/section[3]/div/div[1]/div[2]/div[2]/text(), " ", "")',
                'price_prolong': 'translate(/html/body/section[3]/div/div[1]/div[3]/div[2]/text(), " ", "")',
                'price_change': 'translate(/html/body/section[3]/div/div[1]/div[4]/div[2]/text(), " ", "")',
            },
        )

    def parse(self, response):
        return self.component.parse(response)

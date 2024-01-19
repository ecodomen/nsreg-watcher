# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


class Nsreg_ad100Spider(scrapy.Spider):
    name = 'nsreg_a100'
    allowed_domains = ['a100.ru']
    start_urls = ['https://a100.ru/#overlappable']
    site_names = ("ООО «А100»",)
    custom_settings = {
        'DOWNLOAD_DELAY': 3,
        'RANDOMIZE_DOWNLOAD_DELAY': False
        }

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

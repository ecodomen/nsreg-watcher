# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


class Nsreg_aabSpider(scrapy.Spider):
    name = 'nsreg_aab'
    allowed_domains = ['aab.ru']
    start_urls = ['https://aab.ru/tarifi_na_uslugi.html']
    site_names = ("ООО «ААБ Медиа»",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r".*?(\d+.\d+).*",
            path={
                'price_reg':        'translate(//*[@id="full_story"]/table/tbody/tr[3]/td[2]/text(), " ", "")',
                'price_prolong':    'translate(//*[@id="full_story"]/table/tbody/tr[6]/td[2]/text(), " ", "")',
                'price_change':     'translate(//*[@id="full_story"]/table/tbody/tr[9]/td[2]/text(), " ", "")'
            }
        )

    def parse(self, response):
        return self.component.parse(response)

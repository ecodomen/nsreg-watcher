# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregMaxnameSpider(scrapy.Spider):
    name = 'nsreg_altnames'
    allowed_domains = ['altnames.ru']
    start_urls = ['http://altnames.ru/',]
    site_names = ("ООО «АЛЬТЕРНАТИВА»",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"(\d+)",
            path={
                'price_reg':        'translate(//*[@id="post-10"]/div/div/div/div/section[4]/div/div/div/div[2]/div/table/tbody/tr[1]/td[2]/text(), " ", "")',
                'price_prolong':    'translate(//*[@id="post-10"]/div/div/div/div/section[4]/div/div/div/div[2]/div/table/tbody/tr[2]/td[2]/text(), " ", "")',
                'price_change':     'translate(//*[@id="post-10"]/div/div/div/div/section[4]/div/div/div/div[2]/div/table/tbody/tr[3]/td[2]/text(), " ", "")',
            },
        )

    def parse(self, response):
        return self.component.parse(response)

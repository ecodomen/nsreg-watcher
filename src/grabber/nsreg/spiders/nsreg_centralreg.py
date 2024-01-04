# -*- coding: utf-8 -*-
import scrapy
from ..base_site_spider import BaseSpiderComponent


class NsregCentralregSpider(scrapy.Spider):

    name = "nsreg_centralreg_ru"
    start_urls = ["https://www.centralreg.ru/tarify-i-oplata/"]
    allowed_domains = ("www.centralreg.ru")
    site_names = ("ООО «Перспектива»",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls = self.start_urls,
            allowed_domains = self.allowed_domains,
            site_names = self.site_names,
            regex = r"\s{3}([0-9]{2,3})",
            path = { 
                'price_reg': '/html/body/div[1]/div/div/div/div/div/div/div/div/div/div/article/div/div/div/div/div/table/tbody/tr[4]/td[2]/p/strong/text()',
                'price_prolong': '/html/body/div[1]/div/div/div/div/div/div/div/div/div/div/article/div/div/div/div/div/table/tbody/tr[5]/td[2]/p/strong/text()',
                'price_change': '/html/body/div[1]/div/div/div/div/div/div/div/div/div/div/article/div/div/div/div/div/table/tbody/tr[8]/td[2]/p/strong/text()'
                }
            )

    def parse(self, response):
        return self.component.parse(response)
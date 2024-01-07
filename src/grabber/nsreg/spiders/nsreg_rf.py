import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregRfSpider(scrapy.Spider):
    name = "nsreg_rf"
    start_urls = ["https://rf.ru/domain-prices"]
    allowed_domains = ("rf.ru")
    site_names = ("ООО «ДОМЕНЫ.РФ»",)

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9]*)₽",
            path={
                'price_reg': '/html/body/div/section[1]/div/table/tbody/tr[1]/td[2]/text()',
                'price_prolong': '/html/body/div/section[1]/div/table/tbody/tr[1]/td[3]/text()',
                'price_change': '/html/body/div/section[1]/div/table/tbody/tr[1]/td[4]/text()'
            }
        )

    def parse(self, response):
        return self.component.parse(response)

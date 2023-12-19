import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregDomainerSpider(scrapy.Spider):
    name = "nsreg_domainer.py"
    start_urls = ["https://domainer.ru/info/services"]
    allowed_domains = ("domainer.ru")
    site_names = ("ООО «Домейнер»",)

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            #Вопрос остался лишь по регулярке: нужен ли тут регех?
            regex=r"",
            path={
                'price_reg': '/html/body/div[2]/table/tbody/tr[]/td[2]',
                'price_prolong': '/html/body/div[2]/table/tbody/tr[1]/td[2]',
                'price_change': '/html/body/div[2]/table/tbody/tr[3]/td[2]'
            }
        )

    def parse(self, response):
        return self.component.parse(response)

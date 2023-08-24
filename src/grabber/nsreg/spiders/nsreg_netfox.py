import scrapy

from ..base_site_spider import BaseSpiderComponent

# Пример спайдера для одного сайта
class NsregNetfoxSpider(scrapy.Spider):
    name = "nsreg_netfox"
    start_urls = ["https://netfox.ru/"]
    allowed_domains = ("netfox.ru")
    site_names = ("ООО «НЕТФОКС»")

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9][3]).*",
            path={
                'price_reg': '//*[@id="bbody"]/table/tbody/tr[1]/td[2]/h1/text()[3]',
                'price_prolong': '//*[@id="bbody"]/table/tbody/tr[1]/td[2]/h1/text()[3]',
                'price_change': None
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

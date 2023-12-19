# импорты
import scrapy

from ..base_site_spider import BaseSpiderComponent

# Класс
class NsregMaxnameSpider(scrapy.Spider):
    name = "nsreg_maxname.py"
    start_urls = ["https://maxname.ru/domains/"]
    allowed_domains = ("maxname.ru")
    site_names = ("ООО «МаксНейм»",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Инициализация компонента BaseSpiderComponent с требуемыми параметрами
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9]+)[.,\s]?руб.*",
            path={
                'price_reg': '/html/body/div[1]/div/section/div/table/tbody/tr/td[1]/text()',
                'price_prolong': '/html/body/div[1]/div/section/div/table/tbody/tr[2]/td[1]/text()',
                'price_change': '/html/body/div[1]/div/section/div/table/tbody/tr[5]/td[1]/text()'
            }
        )

    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)
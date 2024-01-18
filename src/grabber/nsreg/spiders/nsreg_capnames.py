import scrapy

from ..base_site_spider import BaseSpiderComponent

REGEX_PATTERN = r".*?([0-9]+)₽"


class NsregCapnamesSpider(scrapy.Spider):
    name = "nsreg_capnames"
    start_urls = ["https://capnames.ru/"]
    allowed_domains = ["capnames.ru"]
    site_names = ("ООО «КАПИТАЛЪ»",)
    custom_settings = {
        'DOWNLOAD_DELAY': 3,
        'RANDOMIZE_DOWNLOAD_DELAY': False
        }

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=REGEX_PATTERN,
            path={
                "price_reg": (
                    'translate('
                    '/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div[2]/div/p[1]/text(), '
                    '"\xa0 ", "")'
                    ),
                "price_prolong": (
                    'translate('
                    '/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/p[1]/text(), '
                    '"\xa0 ", "")'
                    ),
                "price_change": (
                    'translate('
                    '/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div[3]/div/div/div[2]/div/p[1]/text(), '
                    '"\xa0 ", "")'
                    ),
            },
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

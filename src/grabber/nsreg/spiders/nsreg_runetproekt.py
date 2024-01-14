import scrapy

from ..base_site_spider import BaseSpiderComponent


class NsregRunetproektSpider(scrapy.Spider):
    name = 'nsreg_runetproekt'

    start_urls = [
        'https://runetproekt.ru/%d0%bf%d0%b5%d1%80%d0%b5%d1%87%d0%b5%d0%bd%d1%8c-%d0%bf%d1%80%d0%b5%d0%b4%d0%be%d1%81%d1%82%d0%b0%d0%b2%d0%bb%d1%8f%d0%b5%d0%bc%d1%8b%d1%85-%d1%83%d1%81%d0%bb%d1%83%d0%b3-%d0%b8-%d1%82%d0%b0%d1%80/'
    ]
    allowed_domains = [
        'runetproekt.ru',
    ]
    site_names = ('ООО «РунетПроект»',)

    # Конструктор класса
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Инициализация компонента BaseSpiderComponent с требуемыми параметрами
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"(\d+)",
            path={
                'price_reg': 'translate(//*[@id="post-83"]/div/table/tbody/tr[2]/td[2]/span/text(), " ", "")',
                'price_prolong': 'translate(//*[@id="post-83"]/div/table/tbody/tr[3]/td[2]/span/text(), " ", "")',
                'price_change': 'translate(//*[@id="post-83"]/div/table/tbody/tr[6]/td[2]/span/text(), " ", "")',
            },
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

"""
Наименования сайтов: ООО «БЕСТРЕГ», ООО «БИГРЕГ», ООО «ВЕБРЕГ», ООО «ДОМЕНСЕРВИС», ООО «ДОМЕНХОСТ», ООО «КЛИКРЕГ»,
ООО «КЛИКХОСТ», ООО «Нетонлайн», ООО «Онлайнрег», ООО «ОПЕНРЕГ», ООО «ПРИМАХОСТ», ООО «РЕГ.РУ ДОМЕНЫ ХОСТИНГ»,
ООО «Редрег», ООО «РЕНТЕР.РУ», ООО «ТЕЛЕБОРД», ООО «ТЕЛЕХОСТ», ООО «ТОПДОМЕН»

Адреса сайтов: https://www.bestreg24.ru, https://www.bigreg24.ru, https://www.webreg24.ru,
https://www.domenservice.ru, https://www.regdomainhost.ru, https://www.clickreg.ru, https://www.clickhost24.ru,
https://www.neton-line.ru, https://www.online-reg.ru, https://www.open-reg.ru, https://www.prima-host.ru,
http://www.regplanet.ru, https://www.red-reg.ru, https://www.sm-domains.ru, http://telebord24.ru, https://telehost24.ru,
http://topdomenreg24.ru,

"""

import scrapy

from ..base_site_spider import BaseSpiderComponent


class MultiSiteSpider2(scrapy.Spider):
    name = 'multi_site_spider2'

    start_urls = (
        'https://www.bestreg24.ru/price',
        'https://www.bigreg24.ru/price',
        'https://www.webreg24.ru/price',
        'https://www.domenservice.ru/price',
        'https://www.regdomainhost.ru/price',
        'https://www.clickreg.ru/price',
        'https://www.clickhost24.ru/price',
        'https://www.neton-line.ru/price',
        'https://www.online-reg.ru/price',
        'https://www.open-reg.ru/price',
        'https://www.prima-host.ru/price',
        'http://www.regplanet.ru/price',
        'https://www.red-reg.ru/price',
        'https://www.sm-domains.ru/price',
        'http://telebord24.ru/price',
        'https://telehost24.ru/price',
        'http://topdomenreg24.ru/price'
    ),
    allowed_domains = (
        'https://www.bestreg24.ru',
        'https://www.bigreg24.ru',
        'https://www.webreg24.ru',
        'https://www.domenservice.ru',
        'https://www.regdomainhost.ru',
        'https://www.clickreg.ru',
        'https://www.clickhost24.ru',
        'https://www.neton-line.ru',
        'https://www.online-reg.ru',
        'https://www.open-reg.ru',
        'https://www.prima-host.ru',
        'http://www.regplanet.ru',
        'https://www.red-reg.ru',
        'https://www.sm-domains.ru',
        'http://telebord24.ru',
        'https://telehost24.ru',
        'http://topdomenreg24.ru'
    ),
    site_names = (
        'ООО «БЕСТРЕГ»',
        'ООО «БИГРЕГ»',
        'ООО «ВЕБРЕГ»',
        'ООО «ДОМЕНСЕРВИС»',
        'ООО «ДОМЕНХОСТ»',
        'ООО «КЛИКРЕГ»',
        'ООО «КЛИКХОСТ»',
        'ООО «Нетонлайн»',
        'ООО «Онлайнрег»',
        'ООО «ОПЕНРЕГ»',
        'ООО «ПРИМАХОСТ»',
        'ООО «РЕГ.РУ ДОМЕНЫ ХОСТИНГ»',
        'ООО «Редрег»',
        'ООО «РЕНТЕР.РУ»',
        'ООО «ТЕЛЕБОРД»',
        'ООО «ТЕЛЕХОСТ»',
        'ООО «ТОПДОМЕН»'
    )

    # Конструктор класса
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Инициализация компонента BaseSpiderComponent с требуемыми параметрами
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9]+[.,\s])?руб",
            path={
                'price_reg': (
                    '/html/body/div[1]/div[3]/article/section/table[1]/tr/td[1]/article[1]/'
                    'div/table/tr[5]/td[2]/text()'
                ),
                'price_prolong': (
                    '/html/body/div[1]/div[3]/article/section/table[1]/tr/td[1]/article[1]/'
                    'div/table/tr[5]/td[3]/text()'
                ),
                'price_change': (
                    '/html/body/div[1]/div[3]/article/section/table[2]/tr/td[1]/article[2]/'
                    'div/table/tr[10]/td[2]/text()'
                )
            }

        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

"""
Наименования сайтов: ООО «101домен Регистрация Доменов», ООО «Аукцион доменов», ООО «Безопасный регистратор»,
ООО «Быстрый Хостинг», ООО «Гига Хостинг», ООО «Городские Домены», ООО «Дата Плюс», ООО «Дата Сити», ООО «Дом Доменов»,
ООО «Дом Хостинга», ООО «Доменные Сервисы», ООО «Доменный Мастер», ООО «Домены Плюс», ООО «Домены Хостинг»,
ООО «ДОМЕНЫ.РУ», ООО «Домэйн Агент», ООО «Домэйн Груп», ООО «Зона Доменов», ООО «Изи Хостинг», ООО «Магазин Доменов»
АО «Международный сетевой технический центр», ООО «Мир Доменов», ООО «Мир Хостинга», ООО «Мощный Хостинг»,
ООО «Мультирег», ООО «НэтДата», ООО «Опен Домэйнс», ООО «Приват Домэйнс», ООО «Приват Хостинг», ООО «Проф Хостинг»,
ООО «Регио», ООО «Регис», ООО «Регистр 1», ООО «Смарт Домэйнс», ООО «Техно Дата», ООО «Турбо Хостинг»,
ООО «Фабрика Доменов», ООО «ФАЕРФОКС», ООО «Хостинг Парк», ООО «Хот Хостинг», ООО «Центр Доменов», ООО «Ю.РУ»

Адреса сайтов: https://sidename.ru, https://domainauction.ru, https://www.safereg.ru, https://www.speedhosting.ru,
https://www.gigahosting.ru, https://citydomains.ru, https://www.data-plus.ru, https://www.datacity.ru,
https://domainhouse.ru, https://www.domhostinga.ru, https://domainservice.ru, https://domainmaster.ru,
https://domainplus.ru, https://www.domainshosting.ru, https://domains.ru, https://domainagent.ru,
https://domaingroup.ru, https://zonadomenov.ru, https://www.easyhosting.ru, https://domain.ru, https://mstci.ru,
https://mirdomenov.ru, https://www.mirhostinga.ru, https://www.powerhosting.ru, https://www.multireg.ru,
https://www.netdata.ru, https://opendomains.ru, https://privatedomains.ru, https://www.privatehosting.ru,
https://www.profhosting.ru, https://www.regio.ru, https://www.regis.ru, http://registr1.ru, https://smartdomains.ru,
https://www.technodata.ru, https://www.turbohosting.ru, http://domainfactory.ru, http://firefox.ru,
https://www.hostingpark.ru, https://www.hothosting.ru, http://domaincenter.ru, http://yu.ru

"""

import scrapy

from ..base_site_spider import BaseSpiderComponent


class MultiSiteSpider1(scrapy.Spider):
    name = 'multi_site_spider1'

    # Конструктор класса
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Инициализация компонента BaseSpiderComponent с требуемыми параметрами
        self.component = BaseSpiderComponent(
            start_urls=(
                'https://sidename.ru/site/tariffs', 'https://domainauction.ru/site/tariffs',
                'https://www.safereg.ru/site/tariffs', 'https://www.speedhosting.ru/site/tariffs',
                'https://www.gigahosting.ru/site/tariffs', 'https://citydomains.ru/site/tariffs',
                'https://www.data-plus.ru/site/tariffs', 'https://www.datacity.ru/site/tariffs',
                'https://domainhouse.ru/site/tariffs', 'https://www.domhostinga.ru/site/tariffs',
                'https://domainservice.ru/site/tariffs', 'https://domainmaster.ru/site/tariffs',
                'https://domainplus.ru/site/tariffs', 'https://www.domainshosting.ru/site/tariffs',
                'https://domains.ru/site/tariffs', 'https://domainagent.ru/site/tariffs',
                'https://domaingroup.ru/site/tariffs', 'https://zonadomenov.ru/site/tariffs',
                'https://www.easyhosting.ru/site/tariffs', 'https://domain.ru/site/tariffs',
                'https://mstci.ru/site/tariffs', 'https://mirdomenov.ru/site/tariffs',
                'https://www.mirhostinga.ru/site/tariffs', 'https://www.powerhosting.ru/site/tariffs',
                'https://www.multireg.ru/site/tariffs', 'https://www.netdata.ru/site/tariffs',
                'https://opendomains.ru/site/tariffs', 'https://privatedomains.ru/site/tariffs',
                'https://www.privatehosting.ru/site/tariffs', 'https://www.profhosting.ru/site/tariffs',
                'https://www.regio.ru/site/tariffs', 'https://www.regis.ru/site/tariffs',
                'http://registr1.ru/site/tariffs', 'https://smartdomains.ru/site/tariffs',
                'https://www.technodata.ru/site/tariffs', 'https://www.turbohosting.ru/site/tariffs',
                'http://domainfactory.ru/site/tariffs', 'http://firefox.ru/site/tariffs',
                'https://www.hostingpark.ru/site/tariffs', 'https://www.hothosting.ru/site/tariffs',
                'http://domaincenter.ru/site/tariffs', 'http://yu.ru/site/tariffs'
            ),
            allowed_domains=(
                'https://sidename.ru', 'https://domainauction.ru', 'https://www.safereg.ru',
                'https://www.speedhosting.ru', 'https://www.gigahosting.ru', 'https://citydomains.ru',
                'https://www.data-plus.ru', 'https://www.datacity.ru', 'https://domainhouse.ru',
                'https://www.domhostinga.ru', 'https://domainservice.ru', 'https://domainmaster.ru',
                'https://domainplus.ru', 'https://www.domainshosting.ru', 'https://domains.ru',
                'https://domainagent.ru', 'https://domaingroup.ru', 'https://zonadomenov.ru',
                'https://www.easyhosting.ru', 'https://domain.ru', 'https://mstci.ru', 'https://mirdomenov.ru',
                'https://www.mirhostinga.ru', 'https://www.powerhosting.ru', 'https://www.multireg.ru',
                'https://www.netdata.ru', 'https://opendomains.ru', 'https://privatedomains.ru',
                'https://www.privatehosting.ru', 'https://www.profhosting.ru', 'https://www.regio.ru',
                'https://www.regis.ru', 'http://registr1.ru', 'https://smartdomains.ru', 'https://www.technodata.ru',
                'https://www.turbohosting.ru', 'http://domainfactory.ru', 'http://firefox.ru',
                'https://www.hostingpark.ru', 'https://www.hothosting.ru', 'http://domaincenter.ru', 'http://yu.ru'
            ),
            site_names=(
                'ООО «101домен Регистрация Доменов»', 'ООО «Аукцион доменов»', 'ООО «Безопасный регистратор»',
                'ООО «Быстрый Хостинг»', 'ООО «Гига Хостинг»', 'ООО «Городские Домены»', 'ООО «Дата Плюс»',
                'ООО «Дата Сити»', 'ООО «Дом Доменов»', 'ООО «Дом Хостинга»', 'ООО «Доменные Сервисы»',
                'ООО «Доменный Мастер»', 'ООО «Домены Плюс»', 'ООО «Домены Хостинг»', 'ООО «ДОМЕНЫ.РУ»',
                'ООО «Домэйн Агент»', 'ООО «Домэйн Груп»', 'ООО «Зона Доменов»', 'ООО «Изи Хостинг»',
                'ООО «Магазин Доменов»', 'АО «Международный сетевой технический центр»', 'ООО «Мир Доменов»',
                'ООО «Мир Хостинга»', 'ООО «Мощный Хостинг»', 'ООО «Мультирег»', 'ООО «НэтДата»', 'ООО «Опен Домэйнс»',
                'ООО «Приват Домэйнс»', 'ООО «Приват Хостинг»', 'ООО «Проф Хостинг»', 'ООО «Регио»', 'ООО «Регис»',
                'ООО «Регистр 1»', 'ООО «Смарт Домэйнс»', 'ООО «Техно Дата»', 'ООО «Турбо Хостинг»',
                'ООО «Фабрика Доменов»', 'ООО «ФАЕРФОКС»', 'ООО «Хостинг Парк»', 'ООО «Хот Хостинг»',
                'ООО «Центр Доменов»', 'ООО «Ю.РУ»'
            ),

            regex=r"([0-9]+[.,\s])?руб",
            path={
                'price_reg': '/html/body/section/div/div/div/div[2]/div[1]/div[2]/span/text()',
                'price_prolong': '/html/body/section/div/div/div/div[2]/div[2]/div[2]/span/text()',
                'price_change': '/html/body/section/div/div/div/div[2]/div[3]/div[2]/span/text()'
            }

        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)

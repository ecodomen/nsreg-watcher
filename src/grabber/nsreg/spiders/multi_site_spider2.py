'''
Наименования сайтов: ООО «БЕСТРЕГ», ООО «БИГРЕГ», ООО «ВЕБРЕГ», ООО «ДОМЕНСЕРВИС», ООО «ДОМЕНХОСТ», ООО «КЛИКРЕГ»,
ООО «КЛИКХОСТ», ООО «Нетонлайн», ООО «Онлайнрег», ООО «ОПЕНРЕГ», ООО «ПРИМАХОСТ», ООО «РЕГ.РУ ДОМЕНЫ ХОСТИНГ»,
ООО «Редрег», ООО «РЕНТЕР.РУ», ООО «ТЕЛЕБОРД», ООО «ТЕЛЕХОСТ», ООО «ТОПДОМЕН»

Адреса сайтов: https://www.bestreg24.ru, login.php, https://www.bigreg24.ru, login.php,
https://www.webreg24.ru, login.php, https://www.domenservice.ru, login.php, https://www.regdomainhost.ru, login.php,
https://www.clickreg.ru, login.php, https://www.clickhost24.ru, login.php, https://www.neton-line.ru, login.php,
https://www.online-reg.ru, login.php, https://www.open-reg.ru, login.php, https://www.prima-host.ru, login.php,
http://www.regplanet.ru, https://www.red-reg.ru, https://www.sm-domains.ru, login.php, http://telebord24.ru,
https://telehost24.ru, http://topdomenreg24.ru,

'''


import scrapy
from ..items import NsregItem
from ..utils import find_price

REGEX_PATTERN = r"([0-9]+[.,\s])?руб"
EMPTY_PRICE = {
    'pricereg': None,
    'priceprolong': None,
    'pricechange': None,
}


class MultiSiteSpider2(scrapy.Spider):
    name = 'multi_site_spider2'

    def __init__(self, start_urls=None, allowed_domains=None, site_names=None, *args, **kwargs):
        super(MultiSiteSpider2, self).__init__(*args, **kwargs)
        self.start_urls = start_urls.split(',') if start_urls else []
        self.allowed_domains = allowed_domains.split(',') if allowed_domains else []
        self.site_names = site_names.split(',') if site_names else []

    def parse(self, response):
        for i, url in enumerate(self.start_urls):
            pricereg = response.xpath(
                '/html/body/div[1]/div[3]/article/section/table[1]/tr/td[1]/article[1]/div/table/tr[5]/td[2]/text()').get()
            pricereg = find_price(REGEX_PATTERN, pricereg)

            priceprolong = response.xpath(
                '/html/body/div[1]/div[3]/article/section/table[1]/tr/td[1]/article[1]/div/table/tr[5]/td[3]/text()').get()
            priceprolong = find_price(REGEX_PATTERN, priceprolong)

            pricechange = response.xpath(
                '/html/body/div[1]/div[3]/article/section/table[2]/tr/td[1]/article[2]/div/table/tr[10]/td[2]/text()').get()
            pricechange = find_price(REGEX_PATTERN, pricechange)

            item = NsregItem()
            item['name'] = self.site_names[i]
            price = item.get('price', EMPTY_PRICE)
            price['pricereg'] = pricereg
            price['priceprolong'] = priceprolong
            price['pricechange'] = pricechange
            item['price'] = price

            yield item

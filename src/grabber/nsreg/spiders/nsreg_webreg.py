from ..abstract_spider import AbstractSpiderComponent

class NsregWebregSpider(AbstractSpiderComponent):
    name = 'nsreg_webreg'
    allowed_domains = ['www.webreg24.ru']
    start_urls = ['https://www.webreg24.ru/price/']
    site_names = ("ООО «ВЕБРЕГ»",)
    regex = r"([0-9]+[.,\s])?руб"
    path = {
        'price_reg': '//*[@class="b-prices"]/table[1]/tr/td[1]/article[1]/div/table/tr[5]/td[2]/text()',
        'price_prolong': '//*[@class="b-prices"]/table[1]/tr/td[1]/article[1]/div/table/tr[5]/td[3]/text()',
        'price_change': '//*[@class="b-prices"]/table[2]/tr/td[1]/article[2]/div/table/tr[10]/td[2]/text()',
    }

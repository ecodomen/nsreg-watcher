from ..abstract_spider import AbstractSpiderComponent


class NsregThecodeSpider(AbstractSpiderComponent):
    name = "nsreg_thecode"

    allowed_domains = ["thecode.ru"]
    start_urls = ["https://thecode.ru/#price"]
    site_names = ("ООО «КОД»",)

    regex = r"([0-9]+)\s+₽.*"
    path = {
        'price_reg': '//table/tbody/tr[2]/td[2]/div/p/text()',
        'price_prolong': '//table/tbody/tr[3]/td[2]/div/p/text()',
        'price_change': '//table/tbody/tr[4]/td[2]/div/p/text()'
    }

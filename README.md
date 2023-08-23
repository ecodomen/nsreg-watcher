# ngreg-watcher
## Установка
1. Скопируйте репозиторий
2. Установите requirements.txt
3. Установите Sendmail:
```bash
sudo apt install sendemail
```
4. Запустить спайдеры:
```bash 
runspider.sh
```
## Создание спайдера

1.1 Посмотрите пример парсера с использованием композиции:
[src/grabber/nsreg/spiders/nsreg_zonadomenov.py](src/grabber/nsreg/spiders/nsreg_zonadomenov.py)

```
# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


# Пример спайдера для одного сайта
class NsregZonadomenovSpider(scrapy.Spider):
    name = "nsreg_zonadomenov"
    start_urls = ["https://zonadomenov.ru/site/tariffs"]
    allowed_domains = ("zonadomenov.ru")
    # в site_names важно поставить запятую, иначе scrapy вместо целого названия вставит одну букву
    site_names = ("ООО «Зона Доменов»",)

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9]+[.,\s])?руб",
            path={
                'price_reg': 'full/Xpath/1/text()', # например '/html/body/section/div/div/div/div[2]/div[3]/div[2]/span/text()'
                'price_prolong': 'full/Xpath/2/text()', 
                'price_change': 'full/Xpath/3/text()'
            }
        )

    # Метод для обработки ответов на запросы
    def parse(self, response):
        # Применение метода parse компонента BaseSpiderComponent
        return self.component.parse(response)
```

2. Если вам требуется добавить разные регулярные выражения для каждого из полей, то в поле regex записывается такой dict:
```
regex = {
    'price_reg': 'your_regex1',
    'price_prolong': 'your_regex2',
    'price_change': 'your_regex3'
}
```
3. В сложных случаях, когда требуется пройтись по разным страницам внутри сайта, вам необходимо переписать функцию parse. Для прохода по разным страницам лучше всего добавить соответствующую функцию:
```
from nsreg.items import NsregItem()
EMPTY_PRICE = {
    'price_reg': None,
    'price_prolong': None,
    'price_change': None,
}

...

def parse_pricechange(self, response):
        pricechange = response.xpath(self.component.path['price_change']).get()
        pricechange = find_price(, pricechange)

        item = NsregItem()
        item['name'] = "ООО «Ваш ООО»"  
        price = item.get('price', EMPTY_PRICE)
        price['pricechange'] = pricechange
        item['price'] = price
        price['pricechange'] = pricechange 
        item['price'] = price  

        yield item
```
А также вызвать ее из функции parse:
```
def parse(self, response):
    pricereg = response.xpath(self.pathreg).get()
    pricereg = self.find_price(self.regex_reg, pricereg)

    priceprolong = response.xpath(self.pathprolong).get()
    priceprolong = self.find_price(self.regex_prolong, priceprolong)

    yield scrapy.Request('https://2domains.ru/domains/transfer', callback=self.parse_pricechange)

    site_name = self.site_names[0]

    item = NsregItem()
    item['name'] = site_name
    price = item.get('price', EMPTY_PRICE)
    price['price_reg'] = price_reg
    price['price_change'] = price_change
    item['price'] = price
```



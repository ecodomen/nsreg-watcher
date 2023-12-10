# ngreg-watcher
## Установка
1. Скопируйте репозиторий
2. Установите requirements.txt
3. Запустить спайдеры:
```bash
runspider.sh
```
## Создание спайдера
1.1 Разверните приложение, установите зависимости и активируйте env. Инструкция ниже
1.2 В [папке](/home/maria/projects/nsreg-watcher/src/grabber/nsreg/spiders) нужно создать новый парсер с обязательным нэймингом "nsreg_sitename"

2. Посмотрите пример парсера с использованием композиции:
[src/grabber/nsreg/spiders/nsreg_domainshop.py](src/grabber/nsreg/spiders/nsreg_domainshop.py)

3. По аналогии пишете имена, ссылки в классе вашего Спайдера. site_name нужно найти  на сайте регистратора:
```
class NsregDomainshopSpider(scrapy.Spider):
    name = "nsreg_domainshop.py"
    start_urls = ["https://domainshop.ru/services/"]
    allowed_domains = ("domainshop.ru")
    site_names = ("ООО «Лавка доменов»",)
```

4. Подбираете путь к ценам: покупка домена, продление, перенос. Например:
```
'price_reg': '/html/body/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr[1]/td[2]/div/text()',
```
Пути можно посмотреть на сайте и скопировать. Могут возникнуть проблемы с тем, что скопированный путь неправильный -- тогда нужно исследовать его самому
5. Подбираете регулярное выражение (поможет сайт Regex):
```
regex=r"([0-9]+[.,\s])?руб"
```

```
# -*- coding: utf-8 -*-
import scrapy

from ..base_site_spider import BaseSpiderComponent


# Пример спайдера для одного сайта
class NsregDomainshopSpider(scrapy.Spider):
    name = "nsreg_domainshop.py"
    start_urls = ["https://domainshop.ru/services/"]
    allowed_domains = ("domainshop.ru")
    # в site_names важно поставить запятую, иначе scrapy вместо целого названия вставит одну букву
    site_names = ("ООО «Лавка доменов»",)

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.component = BaseSpiderComponent(
            start_urls=self.start_urls,
            allowed_domains=self.allowed_domains,
            site_names=self.site_names,
            regex=r"([0-9]+[.,\s])?руб",
            path={
                'price_reg': '/html/body/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr[1]/td[2]/div/text()',
                'price_prolong': '/html/body/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr[4]/td[2]/div/p/text()',
                'price_change': '/html/body/div/div[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr[7]/td[2]/div/text()'
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

def parse_price_change(self, response):
        price_change = response.xpath(self.component.path['price_change']).get()
        price_change = find_price(, price_change)

        item = NsregItem()
        item['name'] = "ООО «Ваш ООО»"
        price = item.get('price', EMPTY_PRICE)
        price['price_change'] = price_change
        item['price'] = price
        price['price_change'] = price_change
        item['price'] = price

        yield item
```
А также вызвать ее из функции parse:
```
def parse(self, response):
    price_reg = response.xpath(self.pathreg).get()
    price_reg = self.find_price(self.regex_reg, price_reg)

    price_prolong = response.xpath(self.pathprolong).get()
    price_prolong = self.find_price(self.regex_prolong, price_prolong)

    yield scrapy.Request('https://2domains.ru/domains/transfer', callback=self.parse_price_change)

    site_name = self.site_names[0]

    item = NsregItem()
    item['name'] = site_name
    price = item.get('price', EMPTY_PRICE)
    price['price_reg'] = price_reg
    price['price_change'] = price_change
    item['price'] = price
```


# Развертывание приложения на Linux

1. Установите Sendmail, docker, docker-compose
`sudo apt install docker docker-compose`
2. Запустите скрипт по установке зависимостей
`sh install.sh`
	* При возникновении проблем с установкой пакета psycopg2, в файле модифицируйте файл при помощи команды:
	 `sed -i 's/psycopg2/psycopg2-binary/' requirements.txt`
3. Создайте файл окружения `.env` по шаблону `env.template`
4. Запустите PostgreSQL при помощи команд:
`export $(echo $(cat .env | sed 's/#.*//g'| xargs) | envsubst)`
`sudo docker-compose up`
5. Запустите <b>scrapy</b> при помощи команды:
`sh runspiders.sh`
6. Запустите dev-сервер Django при помощи команды:
`sh runsite.sh`

# Развертывание под Windows

## Подготовка системы

Для запуска под виндовс в первую очередь необходимо установить и настроить Windows Subsystem for Linux (WSL). Она доступна в системе по умолчанию начиная с версии 2004 (сборка 19041). Подробнее здесь: https://learn.microsoft.com/ru-ru/windows/wsl/install

Также необходимо установить Docker Desktop (гайд: https://docs.docker.com/desktop/install/windows-install/ )

При скачивании кода проекта обратите внимание на Unix- и Windows-окончания файлов. Рекомендую скачивать через `git clone` либо `git init` + `git remote` + `git pull`, чтобы избежать проблем. Либо воспользуйтесь утилитой dos2unix:
`sudo apt-get install dos2unix`, затем в папке с приложением
`dos2unix *`

## Настройка окружения

1. Установите Sendmail, docker, docker-compose
`sudo apt install sendemail docker docker-compose`
2. Запустите скрипт по установке зависимостей
`bash install.sh`
	* При возникновении проблем с установкой пакета psycopg2, в файле модифицируйте файл при помощи команды:
	 `sed -i 's/psycopg2/psycopg2-binary/' requirements.txt`
3. Создайте файл окружения `.env` по шаблону:
```
# DOCKER-COMPOSE POSTGRES SETTINGS
HOSTNAME_DB=localhost
USERNAME_DB=nsreg
PASSWORD_DB=Nsreg123
DATABASE_NAME=nsreg
PORT_DB=50432
DOCKER_POSTGRES_PORTS_DB=50432:5432

# SENDMAIL SETTINGS
EMAIL_FROM=nsregproject@gmail.com
EMAIL_TO=nsregproject@gmail.com
EMAIL_SMTP=smtp.gmail.com:587
EMAIL_LOGIN=nsregproject@gmail.com
EMAIL_PASS=Nreg123

# DJANGO SETTINGS
DJANGO_SECRET_KEY='django-insecure-5irxqgp-i8c)jp&f3*%ubm(-u@1a3f^fb^_nete-@ixdb3ek4a'
```
4. Запустите PostgreSQL при помощи команд:
`export $(echo $(cat .env | sed 's/#.*//g'| xargs) | envsubst)`
`sudo docker-compose up`
5. Запустите <b>scrapy</b> при помощи команды:
`bash runspiders.sh`
6. Запустите dev-сервер Django при помощи команды:
`bash runsite.sh`

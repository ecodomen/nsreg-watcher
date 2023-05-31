# ngreg-watcher
## Внимание
Посмотрите на свою операционную систему. У меня команды и пути к файлам сделаны для Linux, если у вас Mac/Windows, посмотрите как должны выглядеть команды.
Советую работать на Linux в visual studio code.
Имена переменных 'pricereg', 'priceprolong', 'pricechange' оставляйте такими же.
В неуказанных мною файлах лучше без меня ничего не меняйте. 
Все, что я написала есть в интернете, но ищите информацию на английском. Читайте документацию:

scrapy: https://docs.scrapy.org/en/latest/intro/tutorial.html

python: https://docs.python.org/3/

## Инструкция создания спайдера
0.0 Нужно зарегистрироваться на github, в профиле прописать SSH-ключ: 
https://github.com/settings/keys

0. Клонирует проект на своем компе через github:
```bash
git clone git@github.com:mrezvova/nsreg-watcher.git
``` 

1. Заходите в виртуальное окружение (или создаёте). Здесь для каждой операционной системы свои команды. Посмотрите лучше в интернете.
You can install virtualenv using pip.

Install virtualenv: 
```bash
pip install virtualenv.
``` 

Create virtualenv in the directory you are in: 
```bash
virtualenv <env_name>
``` 

Activate virtualenv: 
```bash
<env_name>\Scripts\activate.
``` 

2. Заходите в папку nsreg-watcher
```bash
cd nsreg-watcher/
``` 

2.1 Посмотрите примеры парсеров в папке:
[src/grabber/nsreg/spiders](/home/rezvov_vadim/projects/nsreg-watcher/src/grabber/nsreg/spiders)

3. Создаёте Спайдер :
```bash
scrapy genspider <имя парсера> <ссылка на сайт>
``` 

4. По аналогии пишете имена, ссылки в классе вашего Спайдера
```python
class Nsreg2domainsSpider(scrapy.Spider):
    name = 'nsreg_2domains'
    allowed_domains = ['2domains.ru']
    start_urls = ['https://2domains.ru/domains']
``` 
4.1 Меняете "ООО «2ДОМЕЙНС.РУ»" на имя соего сайта, который представлен на сайте https://cctld.ru/domains/reg/
```python
item = NsregItem()
item['name'] = "ООО «2ДОМЕЙНС.РУ»"
price = item.get('price', EMPTY_PRICE)
price['pricereg'] = pricereg
price['priceprolong'] = priceprolong
item['price'] = price
```
5. Заходите в: 
```bash
scrapy shell 'ссылка на сайт'
``` 

6. Подбираете путь к ценам: покупка домена, продление, перенос. Например:
```python
def parse_pricechange(self, response):
    pricechange = response.xpath('/html/body/div/div[1]/section[1]/div/div/div/div/div[2]/div[2]/div/span/text()').get()
``` 

7. Подбираете регулярное выражение (поможет сайт Regex)
```python
pricechange = find_price(REGEX_CHANGE_PATTERN, pricechange)
``` 

7.1 Перед использованием reg.expr можно удалить лишние пробельные символы, используя функции, которые лежат в [file](src/grabber/utils.py)
```python
price = str(price).strip()
if m := re.match(re_pattern, price):
    price = m.group(1)
    price = re.sub(r'\s', '', price)
    price = f'{float(price)}'
``` 

7.2  конвертирует во float перед записью в таблицу
```bash
price = f'{float(price)}'
``` 

7.3. все совмещаете в scrapy shell. По шагам проходите обработку цен


8. Записываете п.6 в response.xpath.get()
(/text в конце пути xpath)
```python
pricechange = response.xpath('/html/body/div/div[1]/section[1]/div/div/div/div/div[2]/div[2]/div/span/text()').get()
``` 

9. По аналогии записываете рег.выражение в переменную п.7, если надо несколько переменных создаёте
```python
REGEX_PROLONG_PATTERN = r".*Продление\s+—\s+(([0-9]*[.,])?[0-9]+)\s+₽.*"
REGEX_CHANGE_PATTERN = r".*(([0-9]*[.,])?[0-9]{3})\s+₽.*"
``` 

10. В [launch.json](.vscode/launch.json) записываете имя своего Спайдера вместо 3 строки и нажимаете f5(запускаете пускач, если он у вас не настроен, то можно через терминал п.14)
```bash
"args": [
    "crawl",
    "nsreg_2domains"
],
``` 
Отсюда берёте name(только из своего спайдера)
```python
class Nsreg2domainsSpider(scrapy.Spider):
    name = 'nsreg_2domains'
``` 

11. Отлаживаете, смотрите, есть ли в терминале ошибки. Все ли цены записались, должны быть такие строки в терминале:
```bash
'name': 'ООО «2ДОМЕЙНС.РУ»',
'price': {'pricechange': '799.0',
           'priceprolong': '799.0',
           'pricereg': '149.0'}}
``` 

12. Добавьте запуск своего спайдера в [runspiders.sh](runspiders.sh). Меняете nsreg_2domains на name своего грабера.
```bash 
scrapy crawl nsreg_2domains --logfile $ERROR_LOG --loglevel $LOG_LEVEL
```

13. Если готовы, то делайте commit и укажите меня как получателя на github. Посмотрите как это сделать в вашем обработчике(pycharm скорее всего)

## run crawler
14. Можно запустить спайдера через терминал:

```bash
cd src/grabber/nsreg/
scrapy crawl nsreg
```

install Sendmail:
```bash
sudo apt install sendemail
```
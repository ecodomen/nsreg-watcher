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

1.1 Посмотрите примеры парсеров в папке:
[src/grabber/nsreg/spiders](/home/rezvov_vadim/projects/nsreg-watcher/src/grabber/nsreg/spiders)

2. Есть шаблонные сайты, для которых уже созданы функции в utils_spider.py
В их нейминге первое -- это регион, второе -- это название раздела цен в url
Например, moscow_tariffs()
Пример грабера:
[src/grabber/nsreg/spiders/nsreg_citydomains](/home/rezvov_vadim/projects/nsreg-watcher/src/grabber/nsreg/spiders/nsreg_citydomains)

3. Если сайт не шаблонный, то делайте код идентиным этому:
[src/grabber/nsreg/spiders/nsreg_betnames](/home/rezvov_vadim/projects/nsreg-watcher/src/grabber/nsreg/spiders/nsreg_betnames)

4. Добавьте запуск своего спайдера в [runspiders.sh](runspiders.sh).
```bash 
scrapy crawl nsreg_2domains --logfile $ERROR_LOG --loglevel $LOG_LEVEL
```


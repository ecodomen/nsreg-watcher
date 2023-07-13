# Развертывание приложения

1. Установите Sendmail, docker, docker-compose
`sudo apt install sendemail docker docker-compose`
2. Запустите скрипт по установке зависимостей
`sh install.sh`
	* При возникновении проблем с установкой пакета psycopg2, в файле модифицируйте файл при помощи команды:
	 `sed -i 's/psycopg2/psycopg2-binary/' requirements.txt` 
3. Создайте файл окружения `.env` по шаблону:
```
# DOCKER-COMPOSE POSTGRES SETTINGS
HOSTNAME_DB=localhost
USERNAME_DB=nsreg
PASSWORD_DB=Nsreg123
DATABASE_NAME=nsreg
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
`sh runspiders.sh`
6. Запустите dev-сервер Django при помощи команды:
`sh runsite.sh`

# Развертывание приложения

1. Установите Sendmail, docker, docker-compose
`sudo apt install docker docker-compose python3.10-venv`
2. Запустите скрипт по установке зависимостей
`python3 -m venv env`
`source env/bin/activate`
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

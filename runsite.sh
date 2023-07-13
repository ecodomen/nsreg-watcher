#!/usr/bin/env bash

if [ -f .env ]; then
  export $(echo $(cat .env | sed 's/#.*//g'| xargs) | envsubst)
fi

source env/bin/activate

export PORT_DB=${DOCKER_POSTGRES_PORTS_DB%:*}

python src/website/manage.py makemigrations
python src/website/manage.py migrate
python src/website/manage.py runserver

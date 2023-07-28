# syntax=docker/dockerfile:1
FROM python:3
COPY . /app/
COPY .env /app/
WORKDIR /app
RUN apt-get update
RUN apt-get install -y gettext-base
RUN sh install.sh
RUN export $(echo $(cat .env | sed 's/#.*//g'| xargs) | envsubst)
CMD ["python", "src/telegram_bot"]

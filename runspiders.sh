#!/usr/bin/env bash

if [ -f .env ]; then
  export $(echo $(cat .env | sed 's/#.*//g'| xargs) | envsubst)
fi

source env/bin/activate

ERROR_LOG="$(cd "$(dirname "logs/grabber_errors.log")"; pwd)/$(basename "logs/grabber_errors.log")"
LOG_LEVEL=ERROR
DATE=$(date +”%d-%b-%Y_%H:%M”)
echo "truncating error file:  $ERROR_LOG"
echo -n '' > $ERROR_LOG

cd src/grabber/nsreg

scrapy crawl nsreg --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_2domains --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_aab --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_101domain --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_active_domains --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_a100 --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_altnames --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_ardis --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_atex --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_axelname --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_beget --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_domainauction --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_safe --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_speedhosting --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_webreg --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_domainplus --logfile $ERROR_LOG --loglevel $LOG_LEVEL


if [ ! -s "$ERROR_LOG" ]; then
    echo "Grabber finished without errors."
    sendEmail -f nsregproject@gmail.com         \
            -t nsregproject@gmail.com     \
            -s smtp.gmail.com:587  \
            -xu nsregproject@gmail.com       \
            -xp $pass       \
            -o tls=yes \
            -m "Spiders finished without errors."\
            -u "$DATE: Nsreg grabber finished without errors"
else
    echo "Grabbers finished with errors. Details in $ERROR_LOG"
    sendEmail -f nsregproject@gmail.com         \
            -t nsregproject@gmail.com     \
            -s smtp.gmail.com:587  \
            -xu nsregproject@gmail.com       \
            -xp $pass       \
            -o tls=yes \
            -o message-file=$ERROR_LOG \
            -a $ERROR_LOG \
            -u "$DATE: Nsreg grabber failed with errors"
fi

#!/usr/bin/env bash

source env/bin/activate

ERROR_LOG="$(cd "$(dirname "logs/grabber_errors.log")"; pwd)/$(basename "logs/grabber_errors.log")"
LOG_LEVEL=ERROR
DATE=$(date +”%d-%b-%Y_%H:%M”)
echo "truncating error file:  $ERROR_LOG"
echo -n '' > $ERROR_LOG

cd src/grabber/nsreg

scrapy crawl nsreg --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_2domains --logfile $ERROR_LOG --loglevel $LOG_LEVEL

# scrapy crawl nsreg_aab
# python log.py
# scrapy crawl nsreg_101domain
# scrapy crawl nsreg_a100
# scrapy crawl nsreg_2domains

# scrapy crawl nsreg_2domains --logfile /home/rezvov_vadim/projects/nsreg-watcher/src/grabber/nsreg/write_log.log --loglevel ERROR

if [ ! -s "$ERROR_LOG" ]; then
    echo "Grabber finished without errors."
else
    echo "Grabbers finished with errors. Details in $ERROR_LOG"
    sendEmail -f rezvmaria@gmail.com        \
            -t rezvmaria@gmail.com    \
            -s smtp.gmail.com:587  \
            -xu rezvmaria@gmail.com       \
            -xp rxxmtlhpectgckej       \
            -o tls=yes \
            -o message-file=$ERROR_LOG \
            -a $ERROR_LOG \
            -u "$DATE: Nsreg grabber failed with errors"
fi

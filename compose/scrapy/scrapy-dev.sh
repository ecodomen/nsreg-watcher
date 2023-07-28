#!/usr/bin/env bash
ERROR_LOG="$(cd "$(dirname "logs/grabber_errors.log")"; pwd)/$(basename "logs/grabber_errors.log")"
LOG_LEVEL=ERROR
DATE=$(date +”%d-%b-%Y_%H:%M”)

echo "truncating error file:  $ERROR_LOG"
echo '---SPLIT---' >> $ERROR_LOG

cd src/grabber/nsreg

scrapy list|xargs -n 1 scrapy crawl --logfile $ERROR_LOG --loglevel $LOG_LEVEL

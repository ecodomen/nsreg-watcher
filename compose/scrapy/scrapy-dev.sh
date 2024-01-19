#!/usr/bin/env bash
sleep 10
ERROR_LOG="$(cd "$(dirname "logs/grabber_errors.log")"; pwd)/$(basename "logs/grabber_errors.log")"
LOG_LEVEL=ERROR
DATE=$(date +”%d-%b-%Y_%H:%M”)

echo "truncating error file:  $ERROR_LOG"
echo '---SPLIT---' >> $ERROR_LOG

cd src/grabber/nsreg

scrapy crawl monitor --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy list | awk '$1 != "monitor" {print $1}' | tr '\n' ' ' | xargs scrapy multicrawl --logfile $ERROR_LOG --loglevel $LOG_LEVEL

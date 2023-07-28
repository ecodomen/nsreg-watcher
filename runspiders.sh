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

scrapy list|xargs -n 1 scrapy crawl --logfile $ERROR_LOG --loglevel $LOG_LEVEL

# if [ ! -s "$ERROR_LOG" ]; then
#     echo "Grabber finished without errors."
#     sendEmail -f $EMAIL_FROM                     \
#             -t $EMAIL_TO                         \
#             -s $EMAIL_SMTP                       \
#             -xu $EMAIL_LOGIN                     \
#             -xp $EMAIL_PASS                      \
#             -o tls=yes                           \
#             -m "Spiders finished without errors."\
#             -u "$DATE: Nsreg grabber finished without errors"
# else
#     echo "Grabbers finished with errors. Details in $ERROR_LOG"
#     sendEmail -f $EMAIL_FROM                     \
#             -t $EMAIL_TO                         \
#             -s $EMAIL_SMTP                       \
#             -xu $EMAIL_LOGIN                     \
#             -xp $EMAIL_PASS                      \
#             -o tls=yes                           \
#             -o message-file=$ERROR_LOG           \
#             -a $ERROR_LOG                        \
#             -u "$DATE: Nsreg grabber failed with errors"
# fi

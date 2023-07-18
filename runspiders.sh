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
scrapy crawl nsreg_bigreg --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_mstci --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_nic --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_bestreg --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_bitnames --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_betnames --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_gigahosting --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_citydomains --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_dataplus --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_datacity --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_dns --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_domainhouse --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_mirdomenov --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_domainservice --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_domainmaster --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_domainhosting --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_domeny --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_domains --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_rf --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_domainagent --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_zonadomenov --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_easyhosting --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_domaingroup --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_4it --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_clustered --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_clickhost --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_clickreg --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_domainshop --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_domain --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_klondike --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_masterhost --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_thecode --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_megahost --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_beeline --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_r01 --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_startmail --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_privatedomains --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_opendomains --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_cloudy --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_mirhostinga --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_multiereg --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_netdata --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_salenames --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_smartdomains --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_stepmedia --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_technodata --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_uninic --logfile $ERROR_LOG --loglevel $LOG_LEVEL
scrapy crawl nsreg_spacewebdomains --logfile $ERROR_LOG --loglevel $LOG_LEVEL

if [ ! -s "$ERROR_LOG" ]; then
    echo "Grabber finished without errors."
    sendEmail -f $EMAIL_FROM                     \
            -t $EMAIL_TO                         \
            -s $EMAIL_SMTP                       \
            -xu $EMAIL_LOGIN                     \
            -xp $EMAIL_PASS                      \
            -o tls=yes                           \
            -m "Spiders finished without errors."\
            -u "$DATE: Nsreg grabber finished without errors"
else
    echo "Grabbers finished with errors. Details in $ERROR_LOG"
    sendEmail -f $EMAIL_FROM                     \
            -t $EMAIL_TO                         \
            -s $EMAIL_SMTP                       \
            -xu $EMAIL_LOGIN                     \
            -xp $EMAIL_PASS                      \
            -o tls=yes                           \
            -o message-file=$ERROR_LOG           \
            -a $ERROR_LOG                        \
            -u "$DATE: Nsreg grabber failed with errors"
fi

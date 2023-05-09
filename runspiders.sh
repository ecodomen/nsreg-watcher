#!/usr/bin/env bash

source env/bin/activate

cd src/grabber/nsreg

scrapy crawl nsreg
scrapy crawl nsreg_aab
scrapy crawl nsreg_101domain
scrapy crawl nsreg_a100
scrapy crawl nsreg_2domains


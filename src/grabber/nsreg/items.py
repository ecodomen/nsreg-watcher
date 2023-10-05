# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NsregItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    nic_handle1 = scrapy.Field()
    nic_handle2 = scrapy.Field()
    city = scrapy.Field()
    website = scrapy.Field()
    price = scrapy.Field()

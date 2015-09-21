# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YellowpagesItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    company_name = scrapy.Field()
    # city = scrapy.Field()
    # state = scrapy.Field()
    # zip_code = scrapy.Field()
    telephone = scrapy.Field()
    website = scrapy.Field()
    street = scrapy.Field()
    locality = scrapy.Field()
    region = scrapy.Field()
    postal_code = scrapy.Field()




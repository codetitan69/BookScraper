# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DemobookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BookItem(scrapy.Item):
    title = scrapy.Field()
    category = scrapy.Field()
    description = scrapy.Field()
    prize = scrapy.Field()
    availability = scrapy.Field()
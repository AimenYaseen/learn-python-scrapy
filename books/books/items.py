# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    image_url = scrapy.Field()
    stock = scrapy.Field()
    rating = scrapy.Field()
    description = scrapy.Field()
    UCP = scrapy.Field()
    price_with_tax = scrapy.Field()
    price_without_tax = scrapy.Field()
    tax = scrapy.Field()
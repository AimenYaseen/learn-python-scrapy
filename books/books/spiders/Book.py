import scrapy


class BookSpider(scrapy.Spider):
    name = 'Book'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        pass

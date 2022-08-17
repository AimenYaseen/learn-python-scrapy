import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpBin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/']

    def parse(self, response):
        pass

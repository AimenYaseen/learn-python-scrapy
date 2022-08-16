from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import BooksItem

class BookCrawlerSpider(CrawlSpider):
    name = 'BookCrawler'
    allowed_domains = ['books.toscrape.com']
    base_url = 'http://books.toscrape.com/'
    start_urls = ['http://books.toscrape.com/']

    # def start_requests(self):
    #     yield scrapy.Request('http://books.toscrape.com/', callback=self.parse_filter_book)

    rules = [Rule(LinkExtractor(allow='catalogue/'), callback='parse_filter_book', follow=True)]

    def parse_filter_book(self, response):
        exists = response.css('#product_gallery').get()

        if exists:
           title = response.css('article div h1::text').get()
           price = response.css('article div[class*=product_main] p[class*=price_color]::text').get()
           image_url = self.base_url + response.css('div[class*=item] img::attr(src)').get().replace('../../','')
           stock = response.css('div[class*=product_main] p[class*=instock]::text').getall()[1].strip()
           rating = response.css('div[class*=product_main] p[class*=star]::attr(class)').get().replace('star-rating', '')
           description = response.css('#product_description + p::text').get()
           UCP = response.css('table[class*=table-striped] tr:nth-child(1) td::text').get()
           price_inc_tax = response.css('table[class*=table-striped] tr:nth-child(3) td::text').get()
           price_without_tax = response.css('table[class*=table-striped] tr:nth-child(4) td::text').get()
           tax = response.css('table[class*=table-striped] tr:nth-child(5) td::text').get()
        
           book = BooksItem(
            title = title,
            price = price,
            image_url = image_url,
            stock = stock,
            rating = rating,
            description = description,
            UCP = UCP,
            price_with_tax = price_inc_tax,
            price_without_tax = price_without_tax,
            tax = tax
           )
           yield book
        else:
            print(response.url)
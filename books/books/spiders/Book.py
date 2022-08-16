import scrapy


class BookSpider(scrapy.Spider):
    name = 'Book'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):

        # all_the_books = response.xpath('//article[@class="product_pod"]')
        all_the_books = response.xpath('//article')
        books = response.css('article[class*=product_pod]')

        # Let's loop over the books
        
        # for book in all_the_books:
        #     title = book.xpath('.//h3/a/@title').extract_first()
        #     price = book.xpath('.//div/p[@class="price_color"]/text()').extract_first()
        #     image_url = self.start_urls[0] + book.xpath('.//img[@class="thumbnail"]/@src').extract_first()
        #     book_url = self.start_urls[0] + book.xpath('.//div[@class="image_container"]/a/@href').extract_first()
        #     yield {
        #         'Book Title' : title,
        #         'Book Price' : price,
        #         'Book Image' : image_url,
        #         'Book URL' : book_url
        #     }

        for book in books:
            title = book.css('h3 a[title]::text').get()
            price = book.css('div p[class*=price_color]::text').get()
            image_url = self.start_urls[0] + book.css('img[class*=thumbnail]::attr(src)').get()
            book_url = self.start_urls[0] + book.css('div[class*=image_container] a::attr(href)').get()

            yield {
                'Title' : title,
                'Price' : price,
                'Image Url' : image_url,
                'Book Url' : book_url
            }
        
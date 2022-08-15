import scrapy


class BookSpider(scrapy.Spider):
    name = 'Book'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        all_the_books = response.xpath('//article[@class="product_pod"]')
        # Let's loop over the books
        for book in all_the_books:
            title = book.xpath('.//h3/a/@title').extract_first()
            price = book.xpath('.//div/p[@class="price_color"]/text()').extract_first()
            image_url = self.start_urls[0] + book.xpath('.//img[@class="thumbnail"]/@src').extract_first()
            book_url = self.start_urls[0] + book.xpath('.//div[@class="image_container"]/a/@href').extract_first()
            yield {
                'Book Title' : title,
                'Book Price' : price,
                'Book Image' : image_url,
                'Book URL' : book_url
            }
            # print(title)
            # print(price)
            # print(image_url)
            # print("Book Url : ", book_url)
        

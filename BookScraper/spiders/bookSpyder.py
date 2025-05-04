import scrapy
from BookScraper.items import BookItem

class BookSpider(scrapy.Spider):
    name = "bookSpyder"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css('article')

        for book in books:
            book_page_link = book.css("h3 a::attr(href)").get()

            if book_page_link is not None:
                book_page_link = response.urljoin(book_page_link)
                yield response.follow(book_page_link, callback=self.parse_book_page)

        next_page_link = response.css("li.next a::attr(href)").get()

        if next_page_link is not None:

            # if "catalogue/" in next_page_link:
            #     next_page_link = "https://books.toscrape.com"+next_page_link
            #
            # else:
            #     next_page_link = "https://books.toscrape.com"+"catalogue/"+next_page_link

            next_page_link = response.urljoin(next_page_link)
            yield response.follow(next_page_link,callback=self.parse)


    def parse_book_page(self,response):
        table_rows = response.css(".table.table-striped tr")
        book_item = BookItem()


        book_item["title"] = response.css(".product_main h1::text").get()
        book_item["category"] = response.xpath('//ul[@class="breadcrumb"]/li[@class="active"]/preceding-sibling::li[1]/a/text()').get()
        book_item["description"] = response.xpath('//div[@id="product_description"]/following-sibling::p[1]/text()').get()
        book_item["prize"] = response.css(".product_main p.price_color::text").get()
        book_item["availability"] = table_rows[5].css("td::text").get()


        yield book_item
import scrapy

class ItemSpider(scrapy.Spyder):
    name = "ItemSpyder"
    start_urls = [""]

    def parse(self, response):
        links = response.css("div.row.grid-july a::attr(href)")
        for link in links:
            yield response.follow(link, self.parse_item)
        pass

    def parse_item(self, response):
        yield {
            "name": response.css("div.row h1::text").get(),
            "price": response.css("div.row h2 span.autocalc-product-price::text").get(),
            "outstock": response.css("div.row div.product-description b.outstock::text").get()
        }
        # product_name = response.css("div.row h1::text").get()
        # product_price = response.css("div.row h2 span.autocalc-product-price::text").get()
        # is_outstock = response.css("div.row div.product-description b.outstock::text").get()

        # links response.css("div.row.grid-july a::attr(href)")
        pass
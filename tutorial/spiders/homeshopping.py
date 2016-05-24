import scrapy

from scrapy.crawler import CrawlerProcess
from tutorial.items import ScjItem # items.py
from tutorial.items import LotteItem 

class ScjSpider(scrapy.Spider):
    name = "scj"
    allowed_domains = ["scj.vn"]
    start_urls = [
        "http://www.scj.vn/"
    ]

    def parse(self, response): # looking for links of parent categories
        outer_div = response.xpath('//*[@id="scj_mega"]/div[@class="column "]//h3/a/@href | //*[@id="scj_mega"]/div[@class="column col_last"]//h3/a/@href')

        # After get the list of selectors which contain all links (partial links) of parent categories, we call a callback for each link

        for href in outer_div:
            url = response.urljoin(href.extract())                          # get full link after this line
            yield scrapy.Request(url, callback=self.parse_all_pagination)   # each url is a link to a parent category, each category has many paginations


    def parse_all_pagination(self, response):
        for href in response.css("span.pagination > a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_each_pagination)  # each pagination has many products

    def parse_each_pagination(self, response):                              # get links of all product in each pagination
        for href in response.xpath('//h3[@class="slide_item_title"]/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_product)          # call a callback to parse product in each product link

    def parse_product(self, response):
        item = ScjItem()
        # item['category'] = response.xpath('//*[@id="breadcrum"]/div/a[2]/text()').extract()
        # item['sub_category'] = response.xpath('//*[@id="breadcrum"]/div/a[3]/text()').extract()
        # item['name'] = response.xpath('//div[@class="detailBox"]/h3/text()').extract()
        # item['regular_price'] = response.xpath('//div[@class="detailBox"]//span[@class="col2 price_regular"]/b/text()').extract()
        # item['new_price'] = response.xpath('//div[@class="detailBox"]//span[@class="col2 price"]/text()').extract()[0:1]
        # item['discount'] = response.xpath('//div[@class="detailBox"]//span[@class="col2 price"]/b/text()').extract()
        item['item_link'] = response.url
        item['image_link'] = response.xpath('//*[@id="scj_product_detail"]//img[@id="scjZoom"]/@src').extract()
        # item['description'] = response.xpath('//div[@class="info_wrap"]/*').extract()
        yield item


# # Second spider for LotteDatViet

# class LotteSpider(scrapy.Spider):
#     name = "lotte"
#     allowed_domains = ["scj.vn"]
#     start_urls = [
#         "http://www.scj.vn/"
#     ]

#     def parse(self, response): # looking for links of parent categories
#         outer_div = response.xpath('//*[@id="scj_mega"]/div[@class="column "]//h3/a/@href | //*[@id="scj_mega"]/div[@class="column col_last"]//h3/a/@href')

#         # After get the list of selectors which contain all links (partial links) of parent categories, we call a callback for each link

#         for href in outer_div:
#             url = response.urljoin(href.extract())                          # get full link after this line
#             yield scrapy.Request(url, callback=self.parse_all_pagination)   # each url is a link to a parent category, each category has many paginations


#     def parse_all_pagination(self, response):
#         for href in response.css("span.pagination > a::attr('href')"):
#             url = response.urljoin(href.extract())
#             yield scrapy.Request(url, callback=self.parse_each_pagination)  # each pagination has many products

#     def parse_each_pagination(self, response):                              # get links of all product in each pagination
#         for href in response.xpath('//h3[@class="slide_item_title"]/a/@href'):
#             url = response.urljoin(href.extract())
#             yield scrapy.Request(url, callback=self.parse_product)          # call a callback to parse product in each product link

#     def parse_product(self, response):
#         item = ScjItem()
#         item['category'] = response.xpath('//*[@id="breadcrum"]/div/a[2]/text()').extract()
#         # item['sub_category'] = response.xpath('//*[@id="breadcrum"]/div/a[3]/text()').extract()
#         # item['name'] = response.xpath('//div[@class="detailBox"]/h3/text()').extract()
#         # item['regular_price'] = response.xpath('//div[@class="detailBox"]//span[@class="col2 price_regular"]/b/text()').extract()
#         # item['new_price'] = response.xpath('//div[@class="detailBox"]//span[@class="col2 price"]/text()').extract()[0:1]
#         # item['discount'] = response.xpath('//div[@class="detailBox"]//span[@class="col2 price"]/b/text()').extract()
#         # item['item_link'] = response.url
#         # item['image_link'] = response.xpath('//*[@id="scj_product_detail"]//img[@id="scjZoom"]/@src').extract()
#         # item['description'] = response.xpath('//div[@class="info_wrap"]/*').extract()
#         yield item


# process = CrawlerProcess()
# process.crawl(ScjSpider)
# process.crawl(LotteSpider)
# process.start()

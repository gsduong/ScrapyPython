import scrapy

class ScjItem(scrapy.Item):
	# name = scrapy.Field()
	# sub_category = scrapy.Field()
	category = scrapy.Field()
	# new_price = scrapy.Field()
	# regular_price = scrapy.Field()
	# image_link = scrapy.Field()
	# item_link = scrapy.Field()
	# discount = scrapy.Field()
	# description = scrapy.Field()

class LotteItem(scrapy.Item):
	# name = scrapy.Field()
	# sub_category = scrapy.Field()
	# category = scrapy.Field()
	# new_price = scrapy.Field()
	# regular_price = scrapy.Field()
	image_link = scrapy.Field()
	item_link = scrapy.Field()
	# discount = scrapy.Field()
	# description = scrapy.Field()

class LiveScjItem(scrapy.Item):
	product_link = scrapy.Field()
	
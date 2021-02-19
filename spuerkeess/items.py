import scrapy


class SpuerkeessItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()

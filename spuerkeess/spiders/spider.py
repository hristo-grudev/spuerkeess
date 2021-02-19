import scrapy

from scrapy.loader import ItemLoader
from ..items import SpuerkeessItem
from itemloaders.processors import TakeFirst


class SpuerkeessSpider(scrapy.Spider):
	name = 'spuerkeess'
	start_urls = ['https://www.spuerkeess.lu/fr/a-propos-de-nous/politique-rse/rse-news/']

	def parse(self, response):
		post_links = response.xpath('//div[contains(@class,"timeline-module-content-block")]')
		for post in post_links:
			print(post)
			yield self.parse_post(response, post)

	def parse_post(self, response, post):
		title = post.xpath('.//h4/text()').get()
		description = post.xpath('.//div[@class="timeline-module-description"]//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()

		item = ItemLoader(item=SpuerkeessItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)

		return item.load_item()

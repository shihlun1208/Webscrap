# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, Join, MapCompose
from w3lib.html import remove_tags

class CrawlerTutuAnnaItem(scrapy.Item):
    Url = scrapy.Field()
    Product_Name = scrapy.Field(input_processor=MapCompose, output_process=Join())
    Size_InStock = scrapy.Field(input_processor=MapCompose, output_process=Join())
    Size_OutofStock = scrapy.Field(input_processor=MapCompose, output_process=Join())
    AwooTags = scrapy.Field(input_processor=MapCompose, output_process=Join())

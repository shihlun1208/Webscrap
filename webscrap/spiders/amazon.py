from email import header
import inspect
from tkinter import E
import scrapy
from webscrap.items import CrawlerTutuAnnaItem
from scrapy.loader import ItemLoader
import re
from scrapy_splash import SplashRequest
from scrapy import FormRequest
from scrapy.shell import inspect_response

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    
    start_urls = ['https://www.amazon.com/']

    def parse(self, response, **kwargs):
        URL = response.url
        yield SplashRequest(URL, callback=self.parse_search, args={'wait': 10}) 

    def parse_search(self, response):
        print("Amazon title: \n")
        print(response.css('title::text').get())
        print(response.css('div#hmenu-content'))
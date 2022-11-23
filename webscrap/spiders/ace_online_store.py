from email import header
import inspect
from tkinter import E
import scrapy
from webscrap.items import CrawlerTutuAnnaItem
from scrapy.loader import ItemLoader
import re
from scrapy_splash import SplashRequest, SplashFormRequest
from scrapy import FormRequest
from scrapy.shell import inspect_response

class AceSpider(scrapy.Spider):
    name = 'ace'
    
    start_urls = ['https://store.ace.jp/shop/default.aspx']

    def parse(self, response, **kwargs):
        form_data = {"search": "x","q": "オンオフ"}

        yield SplashFormRequest.from_response(
                response,
                callback=self.parse_search,
                formdata=form_data, 
                args={'wait': 10}) 

    def parse_search(self, response):
        print("URL = ", response.url)

        search_results = response.css("div._searchresults")
        items = search_results.css("div._item")
        for item in items:
            print(item.css("div._title>a::text").get(), item.css("div._title>a").attrib['href'])
        # print(search_page.css('div.searchresults'))
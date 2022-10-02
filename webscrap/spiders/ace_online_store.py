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

class AceSpider(scrapy.Spider):
    name = 'ace'
    
    start_urls = ['https://store.ace.jp/shop/default.aspx']

    def parse(self, response, **kwargs):
        myheader = {"Content-Type": "text/plain"}
        form_data = {"cart":{"items":[]},
                    "section":"cart",
                    "account":"CTX-3V6ctADU",
                    "uid":"cfc96362-2a9c-43f4-bfd2-6a8d004ebdaa",
                    "location":"https://store.ace.jp/shop/pages/search.aspx?search=x&q=%E3%82%AA%E3%83%B3%E3%82%AA%E3%83%95",
                    "referer":""}
        # yield FormRequest.from_response(response,
        #                                 formdata=form_data,
        #                                 callback=self.parse_search)
        
        yield SplashRequest("https://store.ace.jp/shop/pages/search.aspx?search=x&q=%E3%82%AA%E3%83%B3%E3%82%AA%E3%83%95", callback=self.parse_search, args={'wait': 10}) 

    def parse_search(self, response):
        # pass
        search_page = inspect_response(response, self)
        # print(search_page.css('div.searchresults'))
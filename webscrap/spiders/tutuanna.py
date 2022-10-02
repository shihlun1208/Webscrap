import scrapy
from webscrap.items import CrawlerTutuAnnaItem
from scrapy.loader import ItemLoader
import re
from scrapy_splash import SplashRequest

class TutuAnnaSpider(scrapy.Spider):
    name = 'tutuanna'
    
    start_urls = ['https://online.tutuanna.jp/shop/c/c2010/']

    def __init__(self):
        self.base_url = 'https://online.tutuanna.jp'

    def parse(self, response, **kwargs):
        goods_list = response.css("div.goods-list__p")
        for goods_href in goods_list.css("div.goods-list__p-item"):
            href = goods_href.css("p.goods-list__p-item--name a").attrib['href']
            # print("------------------------------------------------------")
            # print(self.base_url + href)
            yield SplashRequest(self.base_url + href, callback=self.parse_goods, args={'wait': 10}) 

    def parse_goods(self, response):
        print("======== URL = {} ========".format(response.url))
        goods_detail = response.css("div.goods-detail-contents")
        # self.itemloader = ItemLoader(item=CrawlerTutuAnnaItem, selector=goods_detail)
        item = CrawlerTutuAnnaItem()
        item["Url"] = response.url
        # self.itemloader["Url"] = response.url
        item["Product_Name"] = self.parse_product_name(goods_detail)
        item["Size_InStock"], item["Size_OutofStock"] = self.parse_size_stock(goods_detail)
        item["AwooTags"] = self.parse_awoo_tags(goods_detail)
        yield item

    def parse_product_name(self, goods_detail):
        return goods_detail.css("h2.ttl-h1.js-enhanced-ecommerce-goods-name::text").get()
    
    def parse_size_stock(self, goods_detail):
        print("======== PARSING SIZE STOCK ========\n")
        variation_list = goods_detail.css('div.goods-detail-variation--list')
        size_in_stock = list()
        size_outof_stock = list()
        if (len(variation_list) > 1):
            # contain image this page
            get_var_list = variation_list[1]
        else:
            get_var_list = variation_list
        for li_tag in get_var_list.css('ul>li.soldout_dgn'):
            print(li_tag.css("a::text").get(), "sold out.")
            size_outof_stock.append(li_tag.css("a::text").get())
        for li_tag in get_var_list.css('ul>li'):
            size_in_stock.append(li_tag.css("a::text").get())
        size_in_stock = list(set(size_in_stock) - set(size_outof_stock))
        print("Size in stock = ", size_in_stock)
        return size_in_stock, size_outof_stock
    
    def parse_awoo_tags(self, goods_detail):
        print("======== PARSING AWOO TAGS ========\n")
        awoo_tags = list()
        good_details_tag = goods_detail.css("div.goods-detail--tag")
        
        print("--------------------------------------------------")
        # for li_tag in good_details_tag.css('ul>li>a::text'):
        #     awoo_tags.append(li_tag.css("a::text").get())\
        return good_details_tag.css('ul>li>a::text').getall()

    
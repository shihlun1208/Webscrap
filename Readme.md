# Scrapy

## Helpful Docs
* [Xpath Cheatsheet](https://devhints.io/xpath)

## Installation
* [python](https://www.python.org/downloads/)
    * `pip install scrapy`
    * `pip install scrapy_splash`
* [docker desktop](https://www.docker.com/products/docker-desktop/)
* [splash](https://splash.readthedocs.io/en/stable/install.html)
    * `docker pull scrapinghub/splash`
    * `docker run -it -p 8050:8050 --rm scrapinghub/splash`
    * [504 Timeout errors](https://splash.readthedocs.io/en/stable/faq.html) \
    `docker run -it -p 8050:8050 --rm scrapinghub/splash --max-timeout 3600`
* [Configuration](https://github.com/scrapy-plugins/scrapy-splash)
    * Follow the github page to config `settings.py`

## Beginner
[Scrapy shell documents](https://docs.scrapy.org/en/latest/topics/shell.html)
```powershell
# Launch scrapy shell
scrapy shell
```

```powershell
# Use splash request
>>> import scrapy_splash
>>> req = scrapy_splash.SplashRequest("https://www.amazon.com/", args={'wait': 10}) 
# Normally, if you are not using splash request you can just `fetch("https://url_wants_to_visit.com")`
>>> fetch(req)
```

```powershell
# grab text of title
>>> response.css('title::text').get()
'Amazon.com. Spend less. Smile more.'
```

```powershell
# grab div class
>>> response.css("div.nav-progressive-content a::text").getall()
['Early Black Friday Deals', 'Disability Customer Support', 'Holiday Gift Guide', 'Best Sellers', 'Amazon Basics', 'Customer Service', 'New Releases', 'Books', 'Music', 'Registry', 'Pharmacy', 'Amazon Home', 'Fashion', 'Gift Cards', 'Toys & Games', 'Kindle Books', 'Sell', 'Coupons', 'Automotive', 'Computers', 'Home Improvement', 'Beauty & Personal Care', 'Video Games', 'Luxury Stores', 'Pet Supplies', 'Health & Household', 'Smart Home', 'Audible', 'Handmade']
```

```powershell
# grab sidebar menu
>>> response.css('div.hmenu-item.hmenu-title::text').getall()
['trending', 'digital content & devices', 'shop by department', 'programs & features', 'help & settings']
```
### Start your first project
[Command line tool documents](https://docs.scrapy.org/en/latest/topics/commands.html)
```powershell
# create project folder
scrapy startproject [yourprojectname]
```
```powershell
# create a spider file
scrapy genspider [spider_filename] [URL_wants_to_crawl]
```
```powershell
# list all your spiders
scrapy list
```
```powershell
# start crawling
scrapy crawl [spider]
```
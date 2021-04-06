import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ScrapingSpider(scrapy.Spider):
    name = 'scraping'
    custom_settings = { 
    'USER_AGENT': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0; 
    }



    def start_requests(self):
        start_urls = [
                    'https://www.kaggle.com/aakashverma8900'
                ]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        data = {}
        for a in response.xpath('//*[@id="profile-container"]'):
            yield response.follow(a, self.parse) 

        
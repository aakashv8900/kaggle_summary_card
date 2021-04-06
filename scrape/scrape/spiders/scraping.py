import scrapy
from scrapy.selector import Selector
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector


class ScrapingSpider(scrapy.Spider):
    name = 'scraping'
    start_urls = ['https://www.kaggle.com/aakashverma8900']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        dive = response.xpath('//div[@id="MathJax_Message""]')
        items = []
        item = DmozItem()
        item["title"] = response.xpath('/html/head/title').extract()
        items.append(item)
        return items

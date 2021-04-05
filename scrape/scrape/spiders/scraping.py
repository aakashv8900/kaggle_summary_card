import scrapy


class ScrapingSpider(scrapy.Spider):
    name = 'scraping'
    start_urls = ['https://www.kaggle.com/aakashverma8900']

    def parse(self, response):
        data={}
        page=response.css('profile-container')
        data['title'] = page.css('div.profile__user-content div.pageheader__title pageheader__title--profile span.profile__head-display-name::text').extract()
        yield data
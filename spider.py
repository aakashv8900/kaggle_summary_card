import scrapy

class KaggleStripper(scrapy.Spider):
    name = 'sasori'
    def __init__(self,response):
        html = response.text

        selector = scrapy.Selector(text = html)


        self.selector = selector


    def start_requests(self):
        
        main_section = self.selector.css(".profile__head-display-name::text")
        print("lol")
        print(main_section.extract())
        

    def parse(self, response):
        
        item = {}
        title = response.css('title::text').get()
        item['title'] = title
        yield item

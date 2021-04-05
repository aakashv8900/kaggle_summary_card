import scrapy

class firstSpider(scrapy.Spider): 
   name = "first" 
   allowed_domains = ["http://kaggle.com"] 
   def parse(self, response): 
    filename = response.url.split("/")[-2] + '.html' 
    with open(filename, 'wb') as f: 
        f.write(response.body)


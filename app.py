import flask 
from flask import request, jsonify
import scrapy
from scrapy.selector import Selector 
from scrapy.http import HtmlResponse

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "hello"


@app.route("/selection")
def selection():
    response = HtmlResponse(url = 'http://kaggle.com') 
    Selector(response = response).xpath('//span/text()').extract()



if __name__ == "__main__":
    app.run(debug=True)
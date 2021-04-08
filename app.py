import flask 
from flask import request, jsonify, render_template
import requests
import json
import scrapy
from scrapy.selector import Selector 
from scrapy.http import HtmlResponse
from scrapy.crawler import CrawlerRunner
from spider import KaggleStripper


app = flask.Flask(__name__)



@app.route("/")
def index():
    return "Heya"



    


@app.route("/api",methods=["GET"])
def api():
    if "user" in request.args:
        complete_url = "https://kaggle.com/"+request.args["user"]
        response = requests.get(complete_url)
        if response.status_code == 200:
            crawler = KaggleStripper(response)
            data = crawler.start_requests()
            sdata = ''.join(list(data))

            print(sdata)
            sdata = sdata.replace("\\","")
            return render_template("card.html",data = sdata)
        return "kaggle profile does not exist"
    return "No user!"


@app.route("/selection",methods=["GET"])
def selection():
    response = HtmlResponse(url = 'http://kaggle.com') 
    f = Selector(response = response).xpath('//span/text()').extract()
    return f



if __name__ == "__main__":
    app.run(debug=True)

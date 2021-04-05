import flask 
from flask import request, jsonify
import requests
import json
import scrapy
from scrapy.selector import Selector 
from scrapy.http import HtmlResponse

app = flask.Flask(__name__)

@app.route("/")
def scrape():


    


@app.route("/api",methods=["GET"])
def api():
    if "user" in request.args:
        return "Welcome "+request.args["user"]
    return "No user!"


@app.route("/selection",methods=["GET"])
def selection():
    response = HtmlResponse(url = 'http://kaggle.com') 
    f = Selector(response = response).xpath('//span/text()').extract()
    return f



if __name__ == "__main__":
    app.run(debug=True)
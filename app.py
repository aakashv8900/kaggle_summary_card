import flask 
from flask import request, jsonify
import requests
import json
import scrapy
from scrapy.selector import Selector 
from scrapy.http import HtmlResponse

app = flask.Flask(__name__)



@app.route("/")
def index():
    return "Heya"



    


@app.route("/api",methods=["GET"])
def api():
    if "user" in request.args:
        response = requests.get("https://kaggle.com/"+request.args["user"])
        if response.status_code == 200:
            print(response.text)
            return "kaggle profile exist"
        return "kaggle profile does not exist"
    return "No user!"


@app.route("/selection",methods=["GET"])
def selection():
    response = HtmlResponse(url = 'http://kaggle.com') 
    f = Selector(response = response).xpath('//span/text()').extract()
    return f



if __name__ == "__main__":
    app.run(debug=True)

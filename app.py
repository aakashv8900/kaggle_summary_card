import flask
from flask import request, jsonify
import requests

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "hello"

@app.route("/api",methods=["GET"])
def api():
    if "user" in request.args:
        response = requests.get("https://kaggle.com/"+request.args["user"])
        if response.status_code == 200:
            print(response.text)
            return "kaggle profile exist"
        return "kaggle profile does not exist"
    return "No user!"





if __name__ == "__main__":
    app.run(debug=True)
import flask
from flask import request, jsonify

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "hello"

@app.route("/api",methods=["GET"])
def api():
    if "user" in request.args:
        return "Welcome "+request.args["user"]
    return "No user!"





if __name__ == "__main__":
    app.run(debug=True)
from mlask import MLAsk
from flask import Flask, render_template, request
from datetime import datetime
import json

emotion_analyzer = MLAsk("-d 'C:/Program Files/MeCab/dic/ipadic'")
app = Flask(__name__)


@app.route("/")
def index():
    return "200 OK"


@app.route("/get-time")
def get_time():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d %H:%M:%S")
    return formatted_time


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/analysis", methods=["POST"])
def analysis():
    json_data = request.json
    print(json_data)
    msg = json_data["message"]
    result = emotion_analyzer.analyze(msg)
    return str(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

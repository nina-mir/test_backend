"""
Event: Google AI Vertex hackathon (July 2023)
Author: Nina Mir | https://github.com/nina-mir
Team: AI 4 literature

Single file server to serve as the backend

reference used for the moods expression : 
https://www.becomeawritertoday.com/list-of-mood-words-for-literature/
"""
import json
from flask import Flask, jsonify, request
from flask_cors import CORS


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})

# loading the backend_data.json
# open article-evergreen.json file
with open("backend_data.json", encoding="utf-8") as data_in:
    data = json.load(data_in)


# sanity check route
@app.route("/ping", methods=["GET"])
def ping_pong():
    """sanity check route"""
    return jsonify("pong!")


# data items GET route
@app.route("/data", methods=["GET"])
def all_data():
    """
    return the entire data set to the frontend
    or if there's a query
    send a filtered JSON to the frontend
    """

    return jsonify(data)

if __name__ == "__main__":
    app.run()

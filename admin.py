import requests
from flask import Flask, request

app = Flask(__name__)

DB_URL = "http://localhost:3000/tracks"

@app.route("/admin/<string:name>", methods=["PUT"])
def add_track(name):
    data = request.get_json()

    if not data or "name" not in data or "artist" not in data or "file" not in data or name != data["name"]:
        return "", 400 # Bad request

    name2 = data["name"]
    artist = data["artist"]
    file = data["file"]
    
    track = { "name":name2, "artist":artist, "file":file }

    response = requests.put(DB_URL, json=track)

    return response.content, response.status_code

@app.route("/admin/<string:name>", methods=["DELETE"])
def delete_track(name):
    data = request.get_json()

    if not data or "name" not in data or "artist" not in data or name != data["name"]:
        return "", 400 # Bad request
    
    name2 = data["name"]
    artist = data["artist"]
    
    track = { "name":name2, "artist":artist }

    response = requests.delete(DB_URL, json=track)

    return response.content, response.status_code

@app.route("/admin", methods=["GET"])
def get_track_names():
    response = requests.get(DB_URL + "_names")

    return response.content, response.status_code

if __name__ == "__main__":
    app.run(host="localhost", port=3001)

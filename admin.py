import requests
import database
from flask import Flask, request

app = Flask(__name__)

DB_URL = "http://localhost:3000/tracks"

@app.route("/admin/<string:name>", methods=["PUT"])
def endpoint1(name):
    data = request.get_json()

    if not data or "name" not in data or "artist" not in data or "file" not in data or name != name2:
        return "", 400 # Bad request

    name2 = data["name"]
    artist = data["artist"]
    file = data["file"]
    
    track = { "name":name, "artist":artist, "file":file }

    response = requests.post(DB_URL, json=track)

    return response.content, response.status_code

if __name__ == "__main__":
    app.run(host="localhost", port=3001)

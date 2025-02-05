import base64
import os
import requests
from flask import Flask, request

app = Flask(__name__)

DB_URL = "http://localhost:3000/tracks"
AUDD_URL = "https://api.audd.io/"
AUDD_API_TOKEN = os.environ["KEY"]

@app.route("/user", methods=["GET"])
def endpoint1():
    data = request.get_json()

    if not data or "fragment" not in data:
        return "", 400 # Bad request

    snippet_wav = base64.b64decode(data["fragment"])

    data = {
        "api_token": AUDD_API_TOKEN,
        "return": "name, artist"
    }

    files = {
        "file": ("snippet.wav", snippet_wav)
    }

    audd_response = requests.post(AUDD_URL, data=data, files=files)

    if audd_response.status_code != 200:
        return audd_response.content, audd_response.status_code
    
    audd_result = audd_response.json()

    recognized_song = audd_result.get("result")

    if not recognized_song:
        return "", 404 # Song not found
    
    recognised_title = recognized_song.get("title")
    recognised_artist = recognized_song.get("artist")

    track = { "name":recognised_title, "artist":recognised_artist }

    db_response = requests.get(DB_URL, json=track)

    return db_response.content, db_response.status_code

if __name__ == "__main__":
    app.run(host="localhost", port=3002)

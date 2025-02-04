import requests
import database
from flask import Flask, request

app = Flask(__name__)

DB_URL = "http://localhost:3000"

@app.route("/admin/<string:name>", methods=["PUT"])
def endpoint1(name):
    js = request.get_json()

    name2 = js["name"]
    artist = js["artist"]
    file = js["file"]

    if not (name2 and artist and file) or name != name2:
        return "", 400  # Bad Request
    
    track = { "name":name, "artist":artist, "file":file }

    insert_url = f"{DB_URL}/tracks"

    return requests.post(insert_url, json=track)

if __name__ == "__main__":
    app.run(host="localhost", port=3001)

import database
from flask import Flask, request

app = Flask(__name__)

@app.route("/admin/<string:name>", methods=["PUT"])
def endpoint1(name):
    js = request.get_json()

    name2 = js["name"]
    artist = js["artist"]
    file = js["file"]

    if name2 != None and artist != None and file != None and name == name2:
        track = { "name":name, "artist":artist, "file":file }

        
    else:
        return "",400 # Bad request
from flask import Flask, jsonify, request
import repository

app = Flask(__name__)

db = repository.Repository("tracks")

@app.route("/tracks", methods=["POST"])
def create_track():
    data = request.get_json()

    if not data or "name" not in data or "artist" not in data or "file" not in data:
        return "", 400 # Bad request
    
    if db.lookup(data["name"], data["artist"]):
        return "", 409 # Conflict - already exists in database
    
    if db.insert(data):
        return "", 201  # Created
    else:
        return "", 500 # Internal server error

if __name__ == "__main__":
    app.run(host="localhost", port=3001)

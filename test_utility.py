import base64

import requests
import database

admin = "http://localhost:3001/admin"

names = [
    "Blinding Lights",
    "Don't Look Back In Anger",
    "Everybody (Backstreet's Back) (Radio Edit)",
    "good 4 u"
]

artists = [
    "The Weeknd",
    "Oasis",
    "Backstreet Boys",
    "Olivia Rodrigo"
]

files = [
    "Blinding Lights",
    "Dont Look Back In Anger",
    "Everybody (Backstreets Back) (Radio Edit)",
    "good 4 u"
]

def populate_database():
    database.db.clear()

    for i in range(len(names)):
        name = names[i]
        artist = artists[i]
        file_path = "songs/" + files[i] + ".wav"

        with open(file_path, "rb") as file:
            file_bytes = file.read()
            encoded_file = base64.b64encode(file_bytes).decode("ascii")

        headers = {
            "Content-Type":"application/json"
        }

        json = {
            "name": name,
            "artist": artist,
            "file": encoded_file
        }

        requests.put(f'{admin}/{name}', headers=headers, json=json)

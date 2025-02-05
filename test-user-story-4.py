import base64
import requests
import unittest
import database

user = "http://localhost:3002/user"
admin = "http://localhost:3001/admin"

class Testing(unittest.TestCase):
    def testCompareGood(self):
        populate_database()

        with open("~Blinding Lights.wav", "rb") as file:
            file_bytes = file.read()
            encoded_file = base64.b64encode(file_bytes).decode("ascii")

        headers = {
            "Content-Type":"application/json"
        }

        json = {
            "fragment": encoded_file
        }

        response = requests.get(f'{user}', headers=headers, json=json)

        if response.status_code != 200:
            self.fail()

        track = response.json()

        with open("temp.wav", "wb") as file:
            file.write(base64.b64decode(track["file"]))

        self.assertEqual(response.status_code, 200)
    
def populate_database():
    database.db.clear()

    name = "Blinding Lights"
    artist = "The Weeknd"
    file_path = "Blinding Lights.wav"

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

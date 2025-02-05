import base64
import requests
import unittest
import database

admin = "http://localhost:3001/admin"

class Testing(unittest.TestCase):
    def testGetGood(self):
        populate_database()

        headers = {
            "Content-Type":"application/json"
        }

        response = requests.get(f'{admin}', headers=headers)

        self.assertEqual(response.status_code, 200)
    
    def testGetEmpty(self):
        headers = {
            "Content-Type":"application/json"
        }

        response = requests.get(f'{admin}', headers=headers)

        self.assertEqual(response.status_code, 404)
    
def populate_database():
    database.db.clear()

    name = "Blinding Lights"
    artist = "The Weekend"
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

import base64
import requests
import unittest
import database

admin = "http://localhost:3000/admin"

class Testing(unittest.TestCase):
    def testInsertionGood(self):
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

        response = requests.put(f'{admin}/{name}', headers=headers, json=json)

        self.assertEqual(response.status_code, 201)

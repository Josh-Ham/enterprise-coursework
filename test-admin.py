import requests
import unittest
import database

admin = "http://localhost:3000/admin"

class Testing(unittest.TestCase):
    def testInsertionGood(self):
        database.db.clear()

        name = "Blinding Lights"
        artist = "The Weekend"
        file = "Blinding Lights.wav"

        headers = {
            "Content-Type":"application/json"
        }

        json = {
            "name": name,
            "artist": artist,
            "file": file
        }

        response = requests.put(f'{admin}/{name}', headers=headers, json=json)

        self.assertEqual(response.status_code, 201)

import base64
import requests
import unittest
import database

admin = "http://localhost:3001/admin"

class Testing(unittest.TestCase):
    def testDeletionGood(self):
        populate_database()

        name = "Blinding Lights"
        artist = "The Weekend"

        headers = {
            "Content-Type":"application/json"
        }

        json = {
            "name": name,
            "artist": artist,
        }

        response = requests.delete(f'{admin}/{name}', headers=headers, json=json)

        self.assertEqual(response.status_code, 204)

    def testDeletionNotExist(self):
        name = "Blinding Lights"
        artist = "The Weekend"

        headers = {
            "Content-Type":"application/json"
        }

        json = {
            "name": name,
            "artist": artist,
        }

        response = requests.delete(f'{admin}/{name}', headers=headers, json=json)

        self.assertEqual(response.status_code, 404)
    
    def testDeletionBadRequestPath(self):
        populate_database()

        name = "Blinding Lights"
        artist = "The Weekend"

        headers = {
            "Content-Type":"application/json"
        }

        json = {
            "name": name,
            "artist": artist,
        }

        response = requests.delete(f'{admin}/{artist}', headers=headers, json=json)

        self.assertEqual(response.status_code, 400)
    
    def testDeletionBadRequest(self):
        populate_database()

        name = "Blinding Lights"

        headers = {
            "Content-Type":"application/json"
        }

        json = {
            "name": name,
        }

        response = requests.delete(f'{admin}/{name}', headers=headers, json=json)

        self.assertEqual(response.status_code, 400)

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
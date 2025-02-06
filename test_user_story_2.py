import requests
import unittest
import testing_utility

admin = "http://localhost:3001/admin"

class Testing(unittest.TestCase):
    def testSuccess(self):
        testing_utility.populate_database()

        name = "Blinding Lights"
        artist = "The Weeknd"

        headers = {
            "Content-Type":"application/json"
        }

        json = {
            "name": name,
            "artist": artist,
        }

        response = requests.delete(f'{admin}/{name}', headers=headers, json=json)

        self.assertEqual(response.status_code, 204)

    def testEmptyError(self):
        testing_utility.database.db.clear()

        name = "Blinding Lights"
        artist = "The Weeknd"

        headers = {
            "Content-Type":"application/json"
        }

        json = {
            "name": name,
            "artist": artist,
        }

        response = requests.delete(f'{admin}/{name}', headers=headers, json=json)

        self.assertEqual(response.status_code, 404)
    
    def testBadPathError(self):
        testing_utility.populate_database()

        name = "Blinding Lights"
        artist = "The Weeknd"

        headers = {
            "Content-Type":"application/json"
        }

        json = {
            "name": name,
            "artist": artist,
        }

        response = requests.delete(f'{admin}/{artist}', headers=headers, json=json)

        self.assertEqual(response.status_code, 400)
    
    def testBadDataError(self):
        testing_utility.populate_database()

        name = "Blinding Lights"

        headers = {
            "Content-Type":"application/json"
        }

        json = {
            "name": name,
        }

        response = requests.delete(f'{admin}/{name}', headers=headers, json=json)

        self.assertEqual(response.status_code, 400)


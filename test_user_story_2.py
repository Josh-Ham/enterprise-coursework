import requests
import unittest
import test_utility

admin = "http://localhost:3001/admin"

class Testing(unittest.TestCase):
    def testSuccess(self):
        test_utility.populate_database()

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
        test_utility.populate_database()

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
        test_utility.populate_database()

        name = "Blinding Lights"

        headers = {
            "Content-Type":"application/json"
        }

        json = {
            "name": name,
        }

        response = requests.delete(f'{admin}/{name}', headers=headers, json=json)

        self.assertEqual(response.status_code, 400)


import base64
import requests
import unittest
import database
import test_utility

user = "http://localhost:3002/user"
admin = "http://localhost:3001/admin"

class Testing(unittest.TestCase):
    def testSuccess(self):
        test_utility.populate_database()

        for i in range(len(test_utility.files)):

            with open("songs/~" + test_utility.files[i] + ".wav", "rb") as file:
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

            with open("temp" + str(i) + ".wav", "wb") as file:
                file.write(base64.b64decode(track["file"]))

            self.assertEqual(response.status_code, 200)

            with open("temp" + str(i) + ".wav", "rb") as temp_file, open("songs/" + test_utility.files[i] + ".wav", "rb") as original:
                self.assertEqual(temp_file.read(), original.read())
    
    def testMissingFragmentError(self):
        test_utility.populate_database()

        headers = {
            "Content-Type": "application/json"
        }
        
        json = {} 

        response = requests.get(f'{user}', headers=headers, json=json)

        self.assertEqual(response.status_code, 400)
    
    def testBadFragmentError(self):
        test_utility.populate_database()

        with open("songs/~Davos.wav", "rb") as file:
            file_bytes = file.read()
            encoded_file = base64.b64encode(file_bytes).decode("ascii")

        headers = {
            "Content-Type":"application/json"
        }

        json = {
            "fragment": encoded_file
        }

        response = requests.get(f'{user}', headers=headers, json=json)

        self.assertEqual(response.status_code, 404)
    
    def testEmptyDatabaseError(self):
        database.db.clear()

        with open("songs/~good 4 u.wav", "rb") as file:
            file_bytes = file.read()
            encoded_file = base64.b64encode(file_bytes).decode("ascii")

        headers = {
            "Content-Type":"application/json"
        }

        json = {
            "fragment": encoded_file
        }

        response = requests.get(f'{user}', headers=headers, json=json)

        self.assertEqual(response.status_code, 404)

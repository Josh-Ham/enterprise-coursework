import base64
from unittest.mock import MagicMock, patch
import requests
import unittest
import database
import test_utility

admin = "http://localhost:3001/admin"

class Testing(unittest.TestCase):
    def testSuccess(self):
        test_utility.populate_database()

        headers = {
            "Content-Type":"application/json"
        }

        response = requests.get(f'{admin}', headers=headers)

        self.assertEqual(response.status_code, 200)
    
    def testEmptyError(self):
        database.db.clear()
        
        headers = {
            "Content-Type":"application/json"
        }

        response = requests.get(f'{admin}', headers=headers)

        self.assertEqual(response.status_code, 404)
    
    def testServiceError(self):
        test_utility.populate_database()
        
        headers = {"Content-Type": "application/json"}
        
        # When a get request made inside admin, replace with the mock object.
        with patch('admin.requests.get') as mock_get:
            fake_response = MagicMock()
            fake_response.status_code = 500
            fake_response.content = ""
            mock_get.return_value = fake_response
            
            response = requests.get(admin, headers=headers)
            self.assertEqual(response.status_code, 500)
    
    def testTimeoutError(self):
        test_utility.populate_database()

        headers = {"Content-Type": "application/json"}
        
        # When a get request made inside admin, replace with the mock object.
        with patch('admin.requests.get', side_effect=requests.exceptions.Timeout):
            response = requests.get(admin, headers=headers)

            self.assertEqual(response.status_code, 500)

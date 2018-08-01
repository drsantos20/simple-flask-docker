import unittest
import sys
sys.path.append('../')
import main
import requests
import json
import sys

###Integration Test
class TestFlaskApiUsingRequests(unittest.TestCase):
    def setUp(self):
        self.app = main.app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_hello_world_error(self):
        response = self.app.post('/')
        self.assertEqual(response.status_code, 400)

###Unit Test
class TestFlaskApi(unittest.TestCase):    
    def test_word_count(self):
        result = main.wordcount("one two three four five")
        self.assertEqual(result, 5)

    def test_word_count_empty(self):
        result = main.wordcount("")
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
import unittest
import sys
sys.path.append('../')
import count
import requests
import json
import sys

class TestFlaskApiUsingRequests(unittest.TestCase):
    def setUp(self):
        self.app = count.app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)


class TestFlaskApi(unittest.TestCase):    
    def test_word_count(self):
        result = count.wordcount("one two three four five")
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
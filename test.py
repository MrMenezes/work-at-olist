import unittest
import app
import requests
import json
import sys


class TestFlaskApiUsingRequests(unittest.TestCase):

  def test_hello_world(self):
    response = requests.get('http://localhost:5000/my-resource/0')
    self.assertEqual(response.json(), {'hello': 'world'})

  def test_post(self):
    response = requests.post('http://localhost:5000/my-resource/0')
    self.assertEqual(response.status_code, 403)


class TestFlaskApi(unittest.TestCase):

  def setUp(self):
    self.app = app.app.test_client()

  def test_hello_world(self):
    response = self.app.get('/my-resource/0')
    self.assertEqual(json.loads(response.get_data().decode(
        sys.getdefaultencoding())), {'hello': 'world'})

  def test_post(self):
    response = self.app.post('/my-resource/0')
    self.assertEqual(response.status_code, 403)

if __name__ == "__main__":
  unittest.main()

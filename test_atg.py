import unittest
import requests

class TestATG(unittest.TestCase):

    def test_atg_website(self):
        url = "https://atg.world/"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

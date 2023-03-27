from selenium import webdriver
import unittest
import logging

class TestWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Windows/System32/chromedriver.exe')
        self.driver.get("https://atg.world/")

    def test_website_load(self):
        title = self.driver.title
        self.assertEqual(title, "ATG - Across The Globe | The Future Of Travel Is Here")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    # Set up logging
    logging.basicConfig(filename='test.log', level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    logging.info("Starting test...")

    unittest.main()

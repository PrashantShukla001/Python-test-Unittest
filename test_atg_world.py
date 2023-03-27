import unittest
import requests
import logging
import xmlrunner

class TestATG(unittest.TestCase):
    
    def setUp(self):
        logging.info("Starting test...")
    
    def test_atg_website(self):
        url = "https://atg.world/"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        logging.info("Website loaded successfully!")
        
    def tearDown(self):
        logging.info("Test complete.")
    
if __name__ == '__main__':
    # Set up logging
    logging.basicConfig(filename='test.log', level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    
    # Run the test and output results in xUnit-style XML format
    with open('test-results.xml', 'wb') as output:
        runner = xmlrunner.XMLTestRunner(output=output)
        unittest.main(testRunner=runner)

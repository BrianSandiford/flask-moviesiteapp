import re
import threading
import unittest
from moviesiteapp import create_app
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SeleniumTestCase(unittest.TestCase):
    client = None

    @classmethod
    def setUpClass(cls):
        # start Firefox
        try:
            cls.client = webdriver.Chrome()
        except:
            pass

        # skip these tests if the browser could not be started
        if cls.client:
            # create the application
            cls.app = create_app('testing')
            cls.app_context = cls.app.app_context()
            cls.app_context.push()

            # suppress logging to keep unittest output clean
            import logging
            logger = logging.getLogger('werkzeug')
            logger.setLevel("ERROR")

            # start the Flask server in a thread
            threading.Thread(target=cls.app.run).start()

    @classmethod
    def tearDownClass(cls):
            if cls.client:
                # stop the flask server and the browser
                cls.client.get('http://localhost:5000/shutdown')
                cls.client.close()
                # remove application context
                cls.app_context.pop()

    def setUp(self):
        if not self.client:
           self.skipTest('Web browser not available')

    def tearDown(self):
        pass

    def test_search(self):
        self.client.get('http://localhost:5000/')
        assert "Movies Website" in self.client.title
        elem = self.client.find_element_by_name("movie_name")
        elem.clear()
        elem.send_keys("Matrix")
        elem.send_keys(Keys.RETURN)
        assert "Not Found" not in self.client.page_source
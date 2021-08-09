import unittest
from  selenium import webdriver
import page
import time

class MovieSiteSearch(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://192.168.1.49:5000/')
    
    def test_search(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "matrix"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()
        


    def tearDown(self):
        time.sleep(5)
        self.driver.close()
    
    
if __name__ == "__main__":
    unittest.main()
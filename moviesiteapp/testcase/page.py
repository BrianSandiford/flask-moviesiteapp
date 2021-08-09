from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = "movie_name"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver



class MainPage(BasePage):
    
    search_text_element = SearchTextElement()
    def is_title_matches(self):
        return "Movies Website" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_FIELD)
        element.send_keys(Keys.RETURN)


class SearchResultPage(BasePage):

    def is_results_found(self):
        return "Not Found" not in self.driver.page_source
        
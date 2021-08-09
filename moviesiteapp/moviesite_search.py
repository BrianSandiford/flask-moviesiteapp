from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://192.168.1.49:5000/")
assert "Movies Website" in driver.title
elem = driver.find_element_by_name("movie_name")
elem.clear()
elem.send_keys("matrix")
elem.send_keys(Keys.RETURN)
assert "Not Found" not in driver.page_source
time.sleep(10)
driver.close()
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

class Search():
    driver = None

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def search_page(self):
        search_Btn = self.driver.find_element_by_id("textview_search").click()
        search_Input = self.driver.find_element_by_id("edittext_search_input")
        search_Text = search_Input.send_keys("반스")
        self.driver.execute_script('mobile:performEditorAction', {'action': 'search'})
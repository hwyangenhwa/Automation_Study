from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Musinsalogin():
    driver = None

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def login_page(self):
        # myPage is launched successfully
        myIcon = self.driver.find_element_by_id("view_mypage").click()
        # loginBtn is launched successfully
        login_Btn = self.driver.find_element_by_id('image_login').click()

        return login_Btn

    def login_inf(self):
        # verify id, pw input box
        ID = self.driver.find_element_by_id("edittext_login_id")
        PW = self.driver.find_element_by_id("edittext_login_pw")
        ID.send_keys("junkune")
        PW.send_keys("sky!20638")

        # verify id, pw input box
        login_Result = self.driver.find_element_by_id("button_login_login")
        login_Result.click()

        return login_Result
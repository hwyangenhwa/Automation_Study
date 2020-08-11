from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Category():
    driver = None

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def category_page(self):
        # access category
        category_Btn = self.driver.find_element_by_id("textview_category").click()

        # 품목, 브랜드, 메뉴 접근
        list_Btn = self.driver.find_element_by_xpath("//androidx.appcompat.app.ActionBar.Tab[@content-desc='품목']").click()
        sleep(2)
        brand_Btn = self.driver.find_element_by_xpath("//androidx.appcompat.app.ActionBar.Tab[@content-desc='브랜드']").click()
        sleep(2)
        menu_Btn = self.driver.find_element_by_xpath("//androidx.appcompat.app.ActionBar.Tab[@content-desc='메뉴']").click()
        sleep(2)
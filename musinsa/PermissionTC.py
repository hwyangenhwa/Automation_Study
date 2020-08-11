from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Permssion():
    driver = None

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def permission_check(self):
        app_Btn = self.driver.find_element_by_id("button_confirm").click()
        alarm_Btn = self.driver.find_element_by_id("button_agree").click()
        sleep(3)

        tel_access = self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
        sleep(3)
        camera_access = self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
        sleep(3)
        media_access = self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button").click()
        sleep(3)

        try:
            # webview chage
            webview = self.driver.contexts[1]
            self.driver.switch_to.context(webview)
            sleep(3)
            btn_Close = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/button[1]").click()

        except NoSuchElementException:
            print("Main View loading")



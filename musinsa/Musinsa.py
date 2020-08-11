from Driver import AppiumDriverSetup
from PermissionTC import Permssion
from LoginTC import Musinsalogin
from PurchaseTC import Purchase
from SearchTC import Search
from CategoryTC import Category
from Utility import UI_Utility
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import HTMLTestRunner
import unittest

class MusinsaTests(unittest.TestCase):
    # permission Flow
    def test_Case1(self):
        driver = AppiumDriverSetup.setUp(self)
        wait = WebDriverWait(driver, 20)

        permissionFlow = Permssion(driver)
        permissionFlow.permission_check()

    # Login Flow
    def test_Case2(self):
        driver = AppiumDriverSetup.setUp(self)
        wait = WebDriverWait(driver, 20)

        try:
            webview_Main = wait.until(EC.visibility_of_element_located((By.ID, "webview_main")))
        except:
            print("Time Session Out")

        loginCheck = Musinsalogin(driver)
        loginField = loginCheck.login_page()
        loginInf = loginCheck.login_inf()

    # Purchase Flow
    def test_Case3(self):
        driver = AppiumDriverSetup.setUp(self)
        wait = WebDriverWait(driver, 20)

        try:
            webview_Main = wait.until(EC.visibility_of_element_located((By.ID, "webview_main")))
        except:
            print("Time Session Out")

        buyFlow = Purchase(driver)
        likeCheck = buyFlow.like_page_Item()
        buyForm = buyFlow.buy_flow()

    # Search Flow
    def test_Case4(self):
        driver = AppiumDriverSetup.setUp(self)
        wait = WebDriverWait(driver, 20)

        try:
            webview_Main = wait.until(EC.visibility_of_element_located((By.ID, "webview_main")))
        except:
            print("Time Session Out")

        searchFlow = Search(driver)
        serachResult = searchFlow.search_page()

    # Category Flow
    def test_Case5(self):
        driver = AppiumDriverSetup.setUp(self)
        wait = WebDriverWait(driver, 20)

        try:
            webview_Main = wait.until(EC.visibility_of_element_located((By.ID, "webview_main")))
        except:
            print("Time Session Out")

        categoryFlow = Category(driver)
        categoryFlow.category_page()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MusinsaTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
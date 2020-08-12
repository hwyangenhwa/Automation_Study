from Driver import AppiumDriverSetup
from PermissionTC import Permssion
from LoginTC import Musinsalogin
from PurchaseTC import Purchase
from SearchTC import Search
from CategoryTC import Category
from Utility import UI_Utility
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HTMLTestRunner
import unittest

class MusinsaTests(unittest.TestCase):
    # permission Flow
    def test_Case1(self):
        driver = AppiumDriverSetup.setUp(self)
        wait = WebDriverWait(driver, 20)

        permissionFlow = Permssion(driver)
        permission_Result = permissionFlow.permission_check()

        if(permission_Result == True):
            print("MainView loading Suceess")
        else:
            print("permission flow is skipped")

        AppiumDriverSetup.tearDown(self)

    # Login Flow
    def test_Case2(self):
        driver = AppiumDriverSetup.setUp(self)
        wait = WebDriverWait(driver, 10)

        try:
            webview_Main = wait.until(EC.visibility_of_element_located((By.ID, "webview_main")))
        except:
            print("Time Session Out")

        try:
            loginCheck = Musinsalogin(driver)
            loginField = loginCheck.login_page()

            if (loginField == True):
                loginInf = loginCheck.login_inf()
            else:
                pass
        except:
            print("is logined")

        AppiumDriverSetup.tearDown(self)

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
    unittest.main(testRunner=HTMLTestRunner.TMLTestRunner(output='test'))

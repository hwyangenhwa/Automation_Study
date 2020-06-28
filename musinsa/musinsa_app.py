'''
Android Native Script
'''
import unittest
import os
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TableSearchTest(unittest.TestCase):
    def setUp(self):
        # Set up appium
        #app = os.path.join(os.path.dirname(__file__), '/Users/junkune.yang/APP', 'MusinsaStore_2.20.1_debug.apk')
        #app = os.path.abspath(app)

        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                #'app': app,
                'platformName' : 'Android',
                'platformVersion' : '9.0',
                'deviceName' : 'Galaxy M20',
                'automationName' : 'Appium',
                'appPackage' : 'com.musinsa.store',
                'appActivity' : 'com.musinsa.store.scenes.deeplink.DeepLinkActivity',
                'noReset' : 'true'
                })

    def test_purchase(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        wait.until(EC.visibility_of_element_located((By.ID, "webview_main")))

        sleep(5)
        like_Btn      = driver.find_element_by_id("view_like").click()

        sleep(3)
        buy_prod      = driver.find_element_by_xpath("//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]").click()

        sleep(5)
        option_Open   = driver.find_element_by_xpath("//android.view.View[3]/android.view.View[@text='구매하기']").click()

        sleep(5)
        select_Opt = driver.find_element_by_id("select-purchase-Layer")
        print(select_Opt)
        option = select_Opt.find_element_by_xpath("//android.widget.Button[@text='옵션 선택']").click()
        print(option)
            #option_Select = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]/android.view.View/android.widget.Button[2]").click()

        sleep(5)
        select = driver.find_element_by_xpath("//android.view.View[3]/android.view.View/android.widget.ListView/android.view.View[1]").click()

        sleep(5)
        driver.find_element_by_xpath("//android.view.View[3]/android.widget.Button[@text='구매하기']").click()

        sleep(5)
        # 구매로 진행하기
        TouchAction(driver).press(x=981, y=1249).move_to(x=991, y=704).release().perform()
        sleep(2)
        TouchAction(driver).press(x=981, y=1249).move_to(x=991, y=704).release().perform()

        sleep(2)
        driver.find_element_by_xpath("/android.widget.Button[@text='가상계좌']").click()

def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TableSearchTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

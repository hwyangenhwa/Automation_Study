from appium import webdriver
import os

class AppiumDriverSetup():
    driver = None

    def setUp(self):
        desired_capabilities = {
            'platformName': 'Android',
            'platformVersion': '10.0',
            'deviceName': 'Pixel 3a XL API 29',
            'app' : '/Users/junkune.yang/APP/MusinsaStore_2.23.0_debug.apk',
            'automationName': 'Appium',
            'appPackage': 'com.musinsa.store',
            'appActivity': 'com.musinsa.store.scenes.deeplink.DeepLinkActivity',
            'automationName': 'UiAutomator2',
            'androidDeviceSocket': "_devtools_remote",
            'chromedriverExecutable': "/Users/junkune.yang/driver/chromedriver",
            'unicodeKeyboard': 'true',
            'resetKeyboard': 'true',
            'noReset': 'true'
       }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities)
        self.driver.implicitly_wait(30)

        return self.driver

        def tearDown(self):
            self.driver.quit()
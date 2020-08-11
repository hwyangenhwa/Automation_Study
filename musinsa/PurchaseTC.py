from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Purchase():
    driver = None

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def like_page_Item(self):
        like_Btn = self.driver.find_element_by_id("view_like").click()
        like_Page = self.wait.until(EC.visibility_of_element_located((By.ID, "view_pager")))

        if(self.driver.find_element_by_id("recycler_view").size != 0):
            like_List = like_Page.find_element_by_id("recycler_view")
            like_Item = like_List.find_element_by_xpath("//android.view.ViewGroup[@index='0']")
            like_Item.click()

            return like_Item
        else:
            print("likepage is not load")

    def buy_flow(self):
        # webview chage
        webview = self.driver.contexts[1]
        self.driver.switch_to.context(webview)
        sleep(3)

        puchase_Btn = self.driver.find_element_by_xpath("//*[@id='btn-purchase-open']/div[2]/a").click()
        option_Btn = self.driver.find_element_by_xpath("//*[@id='goods_opt_area']/button").click()
        size_select_Bttn = self.driver.find_element_by_xpath("//*[@id='option1']/ul/li[1]").click()
        purchase_Result = self.driver.find_element_by_xpath("//*[@id='select-purchase-Layer']/div/div[2]/div[3]/button").click()

        try:
            giftLayer = self.driver.find_element_by_id("getgiftLayer")
            skipBuy_Btn = self.driver.find_element_by_xpath("//*[@id='getgiftLayer']/div/a[2]").click()

        except NoSuchElementException:
            sleep(3)

        # address inf
        address_inf = self.driver.find_element_by_xpath("//*[@id='button_address_org']").click()
        sleep(2)

        # product inf
        product_inf = self.driver.find_element_by_xpath("//*[@id='f1']/div/div[3]/button").click()
        sleep(2)
        
        # coupon inf
        cupon_inf = self.driver.find_element_by_xpath("//*[@id='f1']/div/div[4]/button/i").click()
        sleep(2)

        # purchase inf
        purchase_inf = self.driver.find_element_by_xpath("//*[@id='virtual']/button").click()
        purchase_close = self.driver.find_element_by_xpath("//*[@id='f1']/div/div[5]/button/i").click()
        sleep(2)

        # refund_inf
        refund_inf = self.driver.find_element_by_xpath("//*[@id='f1']/div/div[6]/button/i").click()
        sleep(2)

        # final_inf
        final_inf = self.driver.find_element_by_xpath("//*[@id='f1']/div/div[7]/button/i").click()
        sleep(2)

        # all agree
        all_agree = self.driver.find_element_by_xpath("//*[@id='agree-all']").click()
        sleep(2)

        # puchase gogo
        purchase_gogo = self.driver.find_element_by_xpath("//*[@id='btn_pay']").click()




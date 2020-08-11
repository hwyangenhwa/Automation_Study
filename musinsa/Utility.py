from appium import webdriver

class UI_Utility():
    driver = None

    def __init__(self, driver):
        self.driver = driver
        self.size = driver.get_window_size()

        width = self.size['width']
        height = self.size['height']

    # Swipe right_to_left
    def Left(self):
        start_w = (self.size['width'] / 4) * 3
        end_w = (self.size['width'] / 4)
        start_h = (self.size['height'] / 4) * 3

        self.driver.swipe(start_x= start_w, start_y= start_h, end_x= end_w, end_y= start_h, duration=800)

    # Swipe left_to_right
    def Right(self):
        start_w = (self.size['width'] / 4)
        end_w = (self.size['width'] / 4) * 3
        end_h = (self.size['height'] / 4) * 3

        self.driver.swipe(start_x=start_w, start_y= end_h, end_x=end_w, end_y=end_h, duration=800)

    # Swipe up_to_down
    def Up(self):
        start_w = (self.size['width'] / 4) * 3
        start_h = (self.size['height'] / 4) * 3
        end_h = (self.size['height'] / 4)

        self.driver.swipe(start_x=start_w, start_y=start_h, end_x=start_w, end_y=end_h, duration=800)

    # Swipe_down_to_up
    def Down(self):
        start_w = self.size['width'] / 2
        start_h = (self.size['height'] / 4)
        end_h = (self.size['height'] / 4) * 3

        self.driver.swipe(start_x=start_w, start_y=start_h, end_x=start_w, end_y=end_h, duration=800)



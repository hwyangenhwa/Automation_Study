from selenium import webdriver
import datetime
import re
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import requests
import time

def automate_program(acc, state, inf_Num, roomNumber, checkIn, checkOut):

    # 현재 시각
    current_time = datetime.datetime.now()
    today_time = str(current_time.hour)
    
    # 방번호
    Room_number = roomNumber
    # 변수지정
    Test_ID = 'cine0302@naver.com'
    Test_PW = 'within123!'

    # 정규표현식
    regex = re.compile('[0-9]+')

    #driver = webdriver.Chrome('/Users/movie.yoo/Applications/chromedriver')
    driver = webdriver.Chrome('/Users/jun.k/driver/chromedriver')

    # 여기어때 web 실행 (standby)
    driver.get('https://standby-www.goodchoice.kr')
    driver.implicitly_wait(10)

    # 여기어때 로그인화면 실행
    driver.get('https://standby-www.goodchoice.kr/user/login')
    driver.find_element_by_name('uid').send_keys(Test_ID)
    driver.find_element_by_name('upw').send_keys(Test_PW)
    driver.find_element_by_xpath("//button[@class='btn_link gra_left_right_red']").click()

    # 제휴점 진입
    Test_acc = 'https://standby-www.goodchoice.kr/reservation?adcno='+acc+'&ano='+inf_Num+'&armgno='+roomNumber+'&checkin_type='+state+'&checkin_date='+checkIn+'&checkout_date='+checkOut
    driver.get(Test_acc)

    driver.implicitly_wait(3)
    
    # motel 모텔(대실) & parsing
    try:
        select_time = driver.find_element_by_xpath("//*[@id='usetime']/div[1]/div").text.split("\n")
        number = 0
        
        # 시간을 비교해서 현재시간 선택
        for check_time in select_time:
            number = number + 1
            if (today_time + ":00" == check_time):
                driver.find_element_by_xpath("//*[@id='usetime']/div[1]/div/div["+str(number)+"]/button").click()

    except NoSuchElementException:
        print ("not bab")

    # 예약자 이름
    driver.find_element_by_name("do_user_name").send_keys("test")
    
    # 구매총액 가져오기
    price = driver.find_element_by_xpath("//*[@id='content']/div/div[2]/section[3]/p[1]/b").text.rstrip('원').strip()
    reversation_tmp = regex.match(price).group() + "000"
    reversation_price = int(reversation_tmp)
    
    # 포인트 금액 가져오기
    price = driver.find_element_by_xpath("//*[@id='pointBtn']").text[7:].rstrip("P")
    # 포인트 금액 regex 적용
    point_tmp = reservation_price = regex.match(price).group() + "000"
    point_price = int(point_tmp)

    if (point_price > reversation_price):
        driver.find_element_by_xpath("//*[@id='pointBtn']").click()
        driver.find_element_by_class_name("inp_chk_02").click()
    else:
        print("point~!!")

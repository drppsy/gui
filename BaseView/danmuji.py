from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from data.data import roomids
import random

class OpenChrome():
    def __init__(self):
        #实例化Chrome浏览器
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.douyu.com/1952002")
        self.driver.maximize_window()
        sleep(5)

        # 定位头像元素
        avator = self.driver.find_element_by_css_selector("#js-header > div > div > div.Header-right > div.Header-login-wrap > div > div > a > span")
        ActionChains(self.driver).move_to_element(avator).perform()
        sleep(5)

        # 点击登录
        self.driver.find_element_by_css_selector("#js-header > div > div > div.Header-right > div.Header-login-wrap > div > div > div > div > div > a:nth-child(3)").click()
        sleep(3)

        # 切换到登录弹窗
        iframe = self.driver.find_elements_by_id("login-passport-frame")
        self.driver.switch_to.frame(iframe[0])
        sleep(3)
        # 切到到密码登录
        self.driver.find_element_by_css_selector("#loginbox > div.scancode-login.status-scan.js-scancode-box > div.scanicon-switch-box > div.scanicon-toLogin.js-qrcode-switch").click()
        sleep(1)
        # 切换到昵称登录
        self.driver.find_element_by_css_selector("#loginbox > div.loginNormal.js-login-normal > div.loginbox-bd.loginbox-login > div.loginbox-bd-container > div.loginbox-login-subtype > span:nth-child(3)").click()
        sleep(2)

        # 输入昵称和密码，点击登录
        self.driver.find_element_by_css_selector("#loginbox > div.loginNormal.js-login-normal > div.loginbox-bd.loginbox-login > div.loginbox-bd-container > form > div:nth-child(3) > div > input").send_keys("年小糕啊")
        sleep(1)
        self.driver.find_element_by_css_selector("#loginbox > div.loginNormal.js-login-normal > div.loginbox-bd.loginbox-login > div.loginbox-bd-container > form > div.loginbox-p.login-by-phoneNum.login-by-nickname > input:nth-child(2)").send_keys("212233")
        sleep(2)
        self.driver.find_element_by_css_selector("#loginbox > div.loginNormal.js-login-normal > div.loginbox-bd.loginbox-login > div.loginbox-bd-container > form > div.login-sbt-con > input").click()
        sleep(40)

        #睡40s的期间手动输入手机号的验证码


        for roomid in roomids:
            timer1 = random.randint(9, 12)
            timer2 = random.randint(4, 7)
            url = "https://www.douyu.com/" + str(roomid)
            self.driver.get(url)
            sleep(timer1)

            try:
                self.driver.find_element_by_css_selector(
                    "#js-player-asideMain > div > div.layout-Player-chat > div > div.ChatSpeak > div.ChatSend > textarea").send_keys(
                    "666666！！！233333！哈哈哈哈")
                self.driver.find_element_by_css_selector(
                    "#js-player-asideMain > div > div.layout-Player-chat > div > div.ChatSpeak > div.ChatSend > div.ChatSend-button").click()
                sleep(timer2)
            except:
                continue
            else:
                print('ok')


if __name__ == "__main__":
    run = OpenChrome()

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from data.data import roomids

class OpenChrome():
    def __init__(self):
        #实例化Chrome浏览器
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.douyu.com/18352915")
        self.driver.maximize_window()
        sleep(5)

        if self.driver.find_element_by_css_selector == False:
            print('yes')
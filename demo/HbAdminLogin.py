import unittest
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


class HbAdminLogin(unittest.TestCase):
    def __init__(self, usr, pwd):
        self.usr = usr
        self.pwd = pwd
        self.driver = webdriver.Chrome()

    def test_admin_login(self):
        driver = self.driver
        driver.get("http://admin.app.haibaodatuan.com/login")
        print(driver.title)
        assert "HB Admin" in driver.title
        sleep(1)

        element1 = driver.find_element(by=By.XPATH, value="//input[@type='text']")
        element1.send_keys(self.usr)

        element2 = driver.find_element_by_xpath("//input[@type='password']")
        element2.send_keys(self.pwd)

        driver.find_element_by_xpath("//button[@type='button']").click()
        sleep(2)

        #在谷歌浏览器中copy xpath路径，进入基础功能
        driver.find_element_by_xpath("/html/body/div/ul/li[1]").click()
        sleep(2)

        #在谷歌浏览器中element_copy xpath路径，进入用户管理_用户详情
        driver.find_element_by_xpath("/html/body/div/div/ul/li[2]/ul/li/ul/li[1]/span").click()
        sleep(2)

        #输入1005003用户并点击搜索海豹ID
        element3 = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[1]/input")
        element3.send_keys("1005003")
        driver.find_element_by_xpath("/html/body/div/div/div/div/div/button[1]/span").click()
        sleep(2)

        #在谷歌浏览器中找到element_style_cssPath，复制cssPath，点击奖励惩罚
        driver.find_element_by_css_selector("li:nth-child(2) > ul > li > ul > li:nth-child(2) > span").click()
        sleep(3)

        #关闭浏览器
        driver.close()

if __name__ == "__main__":
    usr = "feta"
    pwd = "212233"
    run = HbAdminLogin(usr, pwd)
    run.test_admin_login()
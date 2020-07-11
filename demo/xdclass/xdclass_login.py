import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class XdClassLogin(unittest.TestCase):
    def __init__(self,usr,pwd):
        #初始化用户名和密码，实例化浏览器
        self.usr = usr
        self.pwd = pwd
        self.driver = webdriver.Chrome()

    def xd_class_login(self):
        #打开浏览器并打印浏览器标题
        driver = self.driver
        driver.get("http://xdclass.net")
        print(driver.title)
        driver.implicitly_wait(3)#隐性等待3s

        #通过css选择器定位到登录并点击登录
        ele1 = driver.find_element_by_css_selector("div#app div.login > span:nth-child(2)")
        sleep(2)#强制等待2s
        ActionChains(driver).click(ele1).perform()
        try:
            # 显性等待5s
            ele5 = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div#app input[type='textt']")))
            print("资源加载成功")
        except:
            print("资源加载失败，发送报警邮件或短信")
        finally:
            print("不管打印是否成功，都打印，用于资源清理")

        #捕捉抓不到元素异常
        try:
            driver.find_element_by_css_selector("div#app input[type='textt']")
        except:
            driver.get_screenshot_as_file("./error.png")
            
        #通过css选择器定位到用户名并输入用户名
        sleep(2)
        ele2 = driver.find_element_by_css_selector("div#app input[type='text']")
        ele2.clear()
        ele2.send_keys(self.usr)

        #通过xpath定位到密码并输入密码
        ele3 = driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[2]/div[2]/div/div[2]/input")
        ele3.clear()
        ele3.send_keys(self.pwd)

        #通过xpath定位到登录button并点击登录
        driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[2]/div[2]/div/div[3]/button").click()

        # #判断是否成功，鼠标移动上面，判断弹窗字符
        # ele4 = driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div[4]/div[3]/img")
        # # ele4 = driver.find_element_by_css_selector("div#app div.avatar.f_r > img")
        # ActionChains(driver).move_to_element(ele4).perform()
        #
        # ele5 = driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div[5]/div/div[1]/p")
        # print(ele5.text)

        #关闭浏览器
        sleep(2)
        driver.close()

if __name__ == "__main__":
    usr = "15618300212"
    pwd = "212233"
    run = XdClassLogin(usr,pwd)
    run.xd_class_login()
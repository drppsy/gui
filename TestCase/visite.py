from BaseView.openchrome import OpenChrome
import time
from time import sleep
import unittest
import HTMLTestRunner

class YxHome(unittest.TestCase):
    def setUp(self):
        #通过GoogleChrome打开网页并选择游犀开发版块
        self.run = OpenChrome()

    def scroll_buttom(self):
        i = 1
        while i < 4:
            self.run.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            sleep(3)
            i += 1
        #滑动到首页最顶部
        self.run.driver.find_element_by_class_name("_back-to-top").click()
        sleep(3)

    def close_buttom(self):
        self.run.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]").click()
        self.run.driver.implicitly_wait(2)

    def home_shift_to_forum(self):
        self.run.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div[1]/div[2]").click()
        self.run.driver.implicitly_wait(2)

    def home_recommended_list(self):
        #滑动到首页推荐的底部再滑上来
        self.scroll_buttom()
        #切换到版块推荐
        self.run.driver.find_elements_by_class_name("_tabs__item")[3].click()
        sleep(2)
        #滑动到版块推荐的底部再滑上来
        self.scroll_buttom()

    def visitor_login(self):
        #游客模式点击登录
        self.run.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/div[3]/div[2]/span[1]").click()
        self.run.driver.implicitly_wait(2)
        self.close_buttom()

        #游客模式点击注册
        self.run.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/div[3]/div[2]/span[2]").click()
        self.run.driver.implicitly_wait(2)
        self.close_buttom()

        #游客模式点击小的登录button
        self.run.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/span").click()
        self.run.driver.implicitly_wait(1)
        self.close_buttom()

        #游客模式点击发布icon
        self.run.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[1]").click()
        self.run.driver.implicitly_wait(1)
        self.close_buttom()

        #游客模式点击我的帖子
        self.run.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/img").click()
        self.run.driver.implicitly_wait(1)
        self.close_buttom()

        #游客模式点击我的草稿
        self.run.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/img").click()
        self.run.driver.implicitly_wait(1)
        self.close_buttom()

        #游客模式点击我的收藏
        self.run.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]").click()
        self.run.driver.implicitly_wait(1)
        self.close_buttom()

        #游客模式点击我的钱包
        self.run.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]").click()
        self.run.driver.implicitly_wait(1)
        self.close_buttom()

        #游客模式点击浏览历史
        self.run.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]").click()
        self.run.driver.implicitly_wait(1)
        self.close_buttom()

        #游客模式首页切换到论坛tab
        self.home_shift_to_forum()
        self.run.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button").click()
        self.run.driver.implicitly_wait(1)
        self.close_buttom()

    def global_search(self):
        #在全局搜索输入“牛”，点击搜索并翻页
        # all_h = self.run.driver.window_handles
        ele1 = self.run.driver.find_element_by_class_name("home-header__input")
        ele1.send_keys("牛")
        self.run.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/div[3]/div[1]/span[1]/div/div/img").click()
        self.run.driver.implicitly_wait(3)



    def tearDown(self):
        #关闭GoogleChrome浏览器
        self.run.driver.close()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    # suite.addTest(YxHome("home_recommended_list"))
    suite.addTest(YxHome("visitor_login"))
    # suite.addTest(YxHome("global_search"))
    # suite.addTest(WapTestcase("test_cancel_an_order"))
    # verbosity参数可以控制执行结果的输出，0是简单报告，1是一般报告，2是详细报告
    # runner = unittest.TextTestRunner(verbosity=1)
    # runner.run(suite)
    #给测试报告文件名加入了时间戳
    file_prefix = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime())
    print(file_prefix)
    #创建测试报告，此时测试报告还是空文件
    #“wb”是指以二进制打开一个文件，只用于写入，如果文件存在则覆盖，不存在则创建
    fp = open("./"+file_prefix+"_result.html","wb")
    #stream定义一个测试报告写入的文件
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="最新的GUI自动化测试报告",description="测试用例执行情况")
    runner.run(suite)
    fp.close()
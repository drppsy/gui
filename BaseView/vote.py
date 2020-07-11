from selenium import webdriver
from time import sleep


class Vote:

    def vote(self):
        #实例化Chrome浏览器
        options = webdriver.ChromeOptions();
        options.add_argument("--auto-open-devtools-for-tabs");
        driver = webdriver.Chrome(options=options)
        driver.get("http://www.shanyueyun.com/index.php?g=Wap&m=Vote&a=index&token=qrrvgp1439540362&id=40&wecha_id=oTJN3wIN1dGpNYXhR2GpARX7Sm_M&sgssz=mp.weixin.qq.com&from=singlemessage")

        windowstabs = driver.window_handles
        driver.switch_to.window(windowstabs[0])
        sleep(3)

        # 选中《抽水马桶的原理》
        driver.find_element_by_css_selector("#slider1 > li > div:nth-child(3) > div > a > img").click()
        sleep(3)

        # 点击确定
        driver.find_element_by_css_selector("#dialogWindow_1100 > footer > div > div:nth-child(1) > a").click()
        sleep(2)

        driver.quit()

    def run_vote(self):
        for i  in range(1000):
            self.vote()
            i += 1

v = Vote()
v.run_vote()
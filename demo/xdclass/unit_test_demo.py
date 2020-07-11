import unittest
import HTMLTestRunner
import time

class XdclassTastcase(unittest.TestCase):
    def setUp(self):
        self.name = "小D课堂"
        self.age = 32
        print("这是前置方法\n")
    def tearDown(self):
        print("这是后置方法\n")
    def test_one(self):
        #测试用例说明，向非专业人说明该用例
        u"这是首页测试用例"
        print("二当家来了")
        self.assertEqual(self.name,"小D课堂",msg="名字不对")
    def test_two(self):
        print("年糕宝宝来了")
        self.assertFalse("feta".isupper(),msg="不是大写")
    def test_three(self):
        print("小狗钱钱来了")
        self.assertEqual("feta".upper(),"FETA")
    def test_four(self):
        print("后端来了")
        self.assertEqual(self.age,32)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(XdclassTastcase("test_three"))
    suite.addTest(XdclassTastcase("test_one"))
    suite.addTest(XdclassTastcase("test_four"))
    suite.addTest(XdclassTastcase("test_two"))
    suite.addTest(XdclassTastcase("test_one"))
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
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="最新的测试报告",description="测试用例执行情况")
    runner.run(suite)
    fp.close()


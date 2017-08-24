# coding=utf-8
import os,time, unittest
import datetime
import HTMLTestRunner
from appium import webdriver


PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class QXmobile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'  # 版本号　
        desired_caps['deviceName'] = 'Default0string'  # 设备名称
        # desired_caps['app']= PATH(r"D:\gitblit\mobile.qixing-group.com\platforms\android\build\outputs\apk\android-x86-debug.apk")　
        desired_caps['appPackage'] = 'hangzhou.qixinggroup.mobile'
        desired_caps['appActivity'] = 'hangzhou.qixinggroup.mobile.MainActivity'

        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app
        print("start app")

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
    #     print("tearDown")

    def switch_tab(self):
        time.sleep(10)
        print("tab----")
        el=self.driver.find_elements_by_class_name("android.view.View")
        el[2].click()
        time.sleep(5)
        count=2
        while count>0:
            el[1].click()
            el[0].click()
            el[1].click()
            el[0].click()
            print(count)
            count=count-1
        print("Success")

    # def refresh_device(self):
    #     self.driver.find_elements_by_class_name("android.view.View")[2].click()
    #     re=self.driver.find_elements_by_class_name("android.view.View")[0].swipe(0,42,1200,1638)



    def test_sleep(self):#用例
        time.sleep(20)
        print("sleep passed")
        

if __name__ == '__main__':
    testunit = unittest.TestSuite()  # 定义一个单元测试容器
    # testunit.addTest(QXmobile("test_sleep"))
    testunit.addTest(QXmobile("switch_tab"))  # 将测试用例加入到测试容器中
    # testunit.addTest(QXmobile("refresh_device"))
    timestr = time.strftime("%Y-%m-%d") #本地日期作为测试报告的名字
    filename = "./"+timestr+".html"
    # filename = "./myAppiumLog.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='QX示教器测试报告',
     description='Report_description')  # 使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
    runner.run(testunit)  # 自动进行测试
    fp.close()

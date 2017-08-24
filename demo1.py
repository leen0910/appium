# coding=utf-8
import os, time, unittest
import HTMLTestRunner
from appium import webdriver

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

class QXmobile(unittest.TestCase):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4'  # 版本号　
    desired_caps['deviceName'] = '0123456789ABCDEF'  # 设备名称
    # desired_caps['app']= PATH(r"D:\gitblit\mobile.qixing-group.com\platforms\android\build\outputs\apk\android-x86-debug.apk")　
    desired_caps['appPackage'] = 'hangzhou.qixinggroup.mobile'
    desired_caps['appActivity'] = 'hangzhou.qixinggroup.mobile.MainActivity'

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)  # 启动app
    time.sleep(40)
    print("sleep passed")

    driver.find_elements_by_class_name("android.view.View")[2].click()
    time.sleep(5)
    count=2
    while count>0:
        driver.find_elements_by_class_name("android.view.View")[1].click()
        driver.find_elements_by_class_name("android.view.View")[0].click()
        driver.find_elements_by_class_name("android.view.View")[1].click()
        driver.find_elements_by_class_name("android.view.View")[1].click()
        print(count)
        count=count-1
    print("Success")
    driver.quit()


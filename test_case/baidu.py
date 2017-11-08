# -*- coding: utf-8 -*-
#unittest框架测试 创建容器并添加用例，细细体会：类（case）
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time
import HTMLTestRunner

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    #测试脚本 类中以test开头的测试用例
    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        # 输入搜索内容
        driver.find_element_by_css_selector("#kw").clear()
        driver.find_element_by_css_selector("#kw").send_keys("2018")
        driver.find_element_by_id("su").click()
    #查找页面元素是否存在
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    #对弹窗异常的处理
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

# if __name__ == "__main__":#执行该语句后无法生成html报告，只能是默认系统执行结果
    # unittest.main()
    # testsuite = unittest.makeSuite()
    #定义一个单元测试容器
    # testunit = unittest.TestSuite()
    #将测试用例加入到测试容器对象中
    # testunit.addTest(Baidu('test_baidu'))
    #报告存放文件路径
    # filename = 'C:\\Python27\\zdh\\report\\result.html'
    # fp = open(filename,'wb')
    #定义测试报告
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title=u'百度测试报告',
    #     description=u'用例执行情况')
    # #运行测试用例
    # runner.run(testunit)
    #定义一个单元测试容器
testunit=unittest.TestSuite()
#将测试用例加入到测试容器中
testunit.addTest(Baidu("test_baidu")) #细细体会：类（case）

#定义个报告存放路径，支持相对路径
filename = 'result.html'
fp = open(filename, 'wb')
#定义测试报告
runner =HTMLTestRunner.HTMLTestRunner(
        stream = fp,
        title = u'百度搜索测试报告',
        description = u'用例执行情况：'
    )
#运行测试用例
runner.run(testunit)

# if __name__ == "__main__":#执行该语句后无法生成html报告，只能是默认系统执行结果，感觉main()内只能执行方法
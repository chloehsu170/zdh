# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.action_chains import ActionChains

class Baidu2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        #搜索设置用例
    def test_baidu2_setting(self):
        u'''百度设置'''
        driver = self.driver
        driver.get(self.base_url+'/')
        driver.find_element_by_link_text("搜索设置").click()
        driver.implicitly_wait(20)
        #点击保存设置
        Select(driver.find_element_by_id("nr")).select_by_visible_text(u"每页显示20条")
        driver.find_element_by_xpath("//input[@value='保存设置']").click()#奇怪只能要xpath识别保存设置
        time.sleep(2)
        #获取网页上的警告信息
        driver.switch_to_alert()#accept()方法是接受并关闭alert，下面无法接受alert内容
        self.assertEqual(u"已经记录下您的使用偏好", self.close_alert_and_get_its_text())
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
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

if __name__ == "__main__":
    unittest.main()

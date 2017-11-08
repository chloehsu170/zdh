#-*-coding:utf-8-*- 
__author__ = 'chloe'
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import time

caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True
driver = webdriver.Firefox(capabilities=caps)
time.sleep(1)
driver.get('http://www.baidu.com')
# driver.find_element_by_id("kw").send_keys(u'春节是哪天')
time.sleep(1)
sbmt = driver.find_element_by_name('tj_login')
print sbmt.text
ActionChains(driver).click_and_hold(sbmt).perform()

#-*-coding:utf-8-*- 
__author__ = 'chloe'

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

# caps = DesiredCapabilities.FIREFOX
# caps["marionette"] = True
# driver = webdriver.Firefox(capabilities=caps)
driver = webdriver.Firefox()
time.sleep(1)
driver.get('http://www.baidu.com')
time.sleep(1)
size = driver.find_element_by_id('kw').size
print size
text = driver.find_element_by_id('cp').text
print text
attr = driver.find_element_by_id('kw').get_attribute('id')
print attr
isDis = driver.find_element_by_id('kw').is_displayed()
print isDis
driver.quit()
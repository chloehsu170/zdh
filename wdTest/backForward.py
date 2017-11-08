#-*-coding:utf-8-*- 
__author__ = 'chloe'

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True
driver = webdriver.Firefox(capabilities=caps)
first_url = 'http://www.baidu.com'
print 'now acess to %s' %(first_url)
driver.get(first_url)
time.sleep(1)
second_url = 'http://news.baidu.com'
print 'now access to %s' %(second_url)
driver.get(second_url)
time.sleep(1)
print 'now back to %s' %(first_url)
driver.back()
time.sleep(1)
print 'now forward to %s' %(second_url)
driver.forward()
time.sleep(1)
# driver.quit()
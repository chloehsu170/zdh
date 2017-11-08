#-*-coding:utf-8-*- 
__author__ = 'chloe'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
title = driver.title
print title
if title == u'百度一下，你就知道':
    print 'title ok'
else:
    print 'title no'
driver.find_element_by_id('kw').send_keys('selenium')
driver.implicitly_wait(20)
driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
time.sleep(2)
driver.find_element_by_id('kw').send_keys(Keys.SPACE)
time.sleep(2)
driver.find_element_by_id('kw').send_keys(u'教程')
time.sleep(2)
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
time.sleep(2)
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
time.sleep(2)
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
url = driver.current_url
print url
if url == 'http://www.baidu.com/':
    print 'url ok'
else:
    print 'url no'
driver.find_element_by_id('su').click()
title = driver.title
print title
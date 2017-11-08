#-*-coding:utf-8-*- 
__author__ = 'chloe'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('selenium')
time.sleep(2)
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

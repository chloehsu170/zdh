#-*-coding:utf-8-*- 
__author__ = 'chloe'

from selenium import webdriver
import time

driver = webdriver.Chrome()
time.sleep(1)
driver.get('http://www.baidu.com')
# driver.find_element_by_name('tj_login').click()
time.sleep(3)
driver.find_element_by_id('kw').clear()
driver.find_element_by_id('kw').send_keys(u'2018年春节是哪天')
driver.find_element_by_id('su').click()
driver.find_element_by_id('su').submit()
time.sleep(2)
driver.find_element_by_name('tj_login').click()
#弹出登录框
driver.find_element_by_id('passport-login-pop').find_element_by_id('TANGRAM__PSP_10__userName').send_keys('xuyanwen')
driver.find_element_by_id('passport-login-pop').find_element_by_name('password').clear()
driver.find_element_by_id('passport-login-pop').find_element_by_name('password').send_keys('111111')
driver.find_element_by_id('passport-login-pop').find_element_by_id('TANGRAM__PSP_10__submit').click()
driver.find_element_by_id('passport-login-pop').find_element_by_id('TANGRAM__PSP_10__submit').submit()
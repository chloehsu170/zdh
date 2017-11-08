#-*-coding:utf-8-*- 
__author__ = 'chloe'
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
time.sleep(1)
driver.find_element_by_id("kw").send_keys(u'春节是哪天')
sbmt = driver.find_element_by_id('su')
# lgn = driver.find_element_by_name('tj_login')
# print lgn.get_attribute('name')
# ActionChains(driver).double_click(sbmt).perform()
ActionChains(driver).context_click(sbmt).perform()

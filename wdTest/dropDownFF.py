#-*-coding:utf-8-*- 
__author__ = 'chloe'
from selenium import webdriver
import os

driver = webdriver.Firefox()
file_path = 'file:///'+ os.path.abspath('drop_down.html')
driver.get(file_path)
aa = driver.find_element_by_id('ShippingMethod')
#二选一，value值要一模一样
# aa.find_element_by_xpath('option[4]').click()
aa.find_element_by_xpath('//option[@value="9.03"]').click()
#debug ok
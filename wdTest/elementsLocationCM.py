#-*-coding:utf-8-*- 
__author__ = 'chloe'

from selenium import webdriver
import os
driver = webdriver.Chrome()
file_path = 'file:///'+ os.path.abspath('checkbox.html')
driver.get(file_path)
# input = driver.find_elements_by_tag_name('input')
# for inputs in input:
#     if inputs.get_attribute('id')== 'c1':
#         inputs.click()
# for inputs in input:
#     if inputs.get_attribute('type')== 'checkbox':
#         inputs.click()
#file:///C:/Python27/zdh/checkbox.html

elements = driver.find_elements_by_css_selector('input[type=checkbox]')
for element in elements:
    element.click()
print len(driver.find_elements_by_css_selector('input[type=checkbox]'))
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
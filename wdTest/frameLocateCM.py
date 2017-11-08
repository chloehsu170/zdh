#-*-coding:utf-8-*- 
__author__ = 'chloe'
from selenium import  webdriver
import os
import time

driver = webdriver.Chrome()
file_path =  'file:///' + os.path.abspath('frame.html')
driver.get(file_path)
driver.implicitly_wait(20)
driver.switch_to_frame('f1')
driver.switch_to_frame('f2')
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(3)
driver.quit()

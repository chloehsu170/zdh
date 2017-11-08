#-*-coding:utf-8-*- 
__author__ = 'chloe'
from selenium import webdriver
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# caps = DesiredCapabilities.FIREFOX
# caps['marionette'] = True
driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('level_locate.html')
driver.get(file_path)
driver.find_element_by_link_text('Link1').click()
aa = driver.find_element_by_id('dropdown1').find_element_by_link_text('Another action')
ActionChains(driver).move_to_element(aa).perform()
WebDriverWait(driver,10).until(lambda x:x.driver.find_element_by_id('dropdown1'))
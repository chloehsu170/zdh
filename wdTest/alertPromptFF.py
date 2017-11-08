#-*-coding:utf-8-*- 
__author__ = 'chloe'
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.maximize_window()
driver.find_element_by_id('kw').clear()
driver.find_element_by_id('kw').send_keys(u'20')
driver.find_element_by_id('su').click()
driver.find_element_by_id('su').submit()
#点击打开搜索设置（选择1）
# driver.find_element_by_link_text("tj_settingicon").click()
#move to element自动展开选项（选择2）
aa = driver.find_element_by_name("tj_settingicon")
ActionChains(driver).move_to_element(aa).perform()
driver.implicitly_wait(20)
driver.find_element_by_link_text("搜索设置").click()
driver.implicitly_wait(20)
#点击保存设置
driver.find_element_by_link_text("保存设置").click()
time.sleep(2)
#获取网页上的警告信息
alert = driver.switch_to_alert()
time.sleep(2)
#接收警告信息
# alert.accept()
#打印警告信息并关闭
print alert.text
alert.dismiss()
driver.quit()
#debug ok
#-*-coding:utf-8-*- 
__author__ = 'chloe'

from selenium import webdriver
import os,time
driver = webdriver.Firefox()
#打开上传文件页面
file_path = 'file:///' + os.path.abspath('upload.html')
driver.get(file_path)
#定位上传按钮，添加本地文件
driver.find_element_by_name("file").send_keys('C:\\LibAntiPrtSc_ERROR.log')
time.sleep(2)
driver.quit()
#send_keys()方法除可以输入内容外，也可以跟一个本地的文件路径
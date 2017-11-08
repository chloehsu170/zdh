#-*-coding:utf-8-*- 
__author__ = 'chloe'
# import requests
# print requests.head('http://www.baidu.com').headers['content-type']
#text/html
import os
from selenium import  webdriver

fp = webdriver.FirefoxProfile()
fp.set_preference('driver.download.folderList',2)
fp.set_preference('driver.download.manager.showWhenStarting',False)
fp.set_preference('driver.download.dir',os.getcwd())
fp.set_preference('driver.helperApps.nerverAsk.saveToDisk','application/octet-stream')
driver = webdriver.Firefox(firefox_profile=fp)
driver.get("http://pypi.python.org/pypi/selenium")
driver.implicitly_wait(20)
driver.find_element_by_link_text('selenium-3.7.0.tar.gz (md5) ').click()
# driver.get("http://www.zimuku.net/detail/96331.html")
# driver.implicitly_wait(20)
# driver.find_element_by_class_name('dl').click()
#下载文件需要配置firefox的profile
# Message: Unable to locate element: {"method":"link text","selector":"selenium-3"}
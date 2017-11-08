#-*-coding:utf-8-*- 
__author__ = 'chloe'

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True
driver = webdriver.Firefox(capabilities=caps)
driver.get("http://m.mail.10086.cn")
#参数数字为像素点
print "设置浏览器宽480、高800显示"
driver.set_window_size(480,800)
time.sleep(2)
driver.quit()
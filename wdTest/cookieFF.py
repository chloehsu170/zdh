#-*-coding:utf-8-*- 
__author__ = 'chloe'
#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.youdao.com")
#向cookie 的name 和value 添加会话信息。
driver.add_cookie({'name':'key-aaaaaaa', 'value':'value-bbbb'})
#遍历cookies 中的name 和value 信息打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print "%s -> %s" % (cookie['name'], cookie['value'])
# 获得cookie 信息
# cookie= driver.get_cookies()
#将获得cookie 的信息打印
# print cookie
# 删除一个特定的cookie
driver.delete_cookie("key-aaaaaaa")
for cookie in driver.get_cookies():
    print "%s -> %s" % (cookie['name'], cookie['value'])
print
# 删除所有cookie
driver.delete_all_cookies()
for cookie in driver.get_cookies():
    print "%s --> %s" % (cookie['name'],cookie['value'])
driver.quit()
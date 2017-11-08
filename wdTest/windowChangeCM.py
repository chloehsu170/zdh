#-*-coding:utf-8-*- 
__author__ = 'chloe'

from selenium import webdriver
import time

driver = webdriver.Chrome()
time.sleep(1)
driver.get('https://www.baidu.com')
time.sleep(3)
driver.find_element_by_id('kw').clear()
driver.find_element_by_id('kw').send_keys(u'2018年春节是哪天')
driver.find_element_by_id('su').click()
driver.find_element_by_id('su').submit()
time.sleep(3)
nowhandle = driver.current_window_handle
driver.implicitly_wait(20)
driver.find_element_by_name('tj_login').click()
#弹出登录框
m = driver.find_element_by_id('passport-login-pop')
m.find_element_by_link_text('立即注册').click()
handles = driver.window_handles
#切换到注册窗口
for handle in handles:
    if handle != nowhandle:
        driver.switch_to_window(handle)
        driver.find_element_by_id('TANGRAM__PSP_3__userName').send_keys('xuyanwen')
        time.sleep(3)
        driver.close()
#切换到百度查询窗口
driver.switch_to_window(nowhandle)
#debug ok 二次定位可以使用变量替代第一次定位

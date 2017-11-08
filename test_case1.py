#-*-coding:utf-8-*-
#根据测试时间生成测试报告，使用HTMLTestRunner生成html测试报告，引入test_case包（必须包含_init_文件）
__author__ = 'chloe'
import unittest
import HTMLTestRunner
from test_case import test_baidu2
from test_case import test_youdao
import time
#创建容器
unitsuite = unittest.TestSuite()
#向容器里添加测试用例
unitsuite.addTest(unittest.makeSuite(test_baidu2.Baidu2))
unitsuite.addTest(unittest.makeSuite(test_youdao.Youdao))
#定义个报告存放路径，支持相对路径
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime())
filename = 'c:\\Python27\\zdh\\report\\'+now+ 'result.html'
fp = open(filename, 'wb')
# 定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'百度搜索测试报告',
        description=u'用例执行情况：'
)
# 运行测试用例
runner.run(unitsuite)
#执行测试套件,类().方法()
# runner = unittest.TextTestRunner()
# runner.run(unitsuite)
# unittest.TextTestRunner().run(unitsuite)


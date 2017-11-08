#-*-coding:utf-8-*-
#测试结果输出到log文档
__author__ = 'chloe'
import os
os.path.getatime("C:\\Python27\\zdh\\test_case\\result.html")
caselist=os.listdir('C:\\Python27\\zdh\\test_case')
for a in caselist:
    s=a.split('.')[1]
    if s=='py':
        os.system('C:\\Python27\\zdh\\test_case\\%s 1>>log.txt 2>&1'%a)
        # 2>&1标准错误输出重定向等同于 标准输出 >>表示追加到log.txt中不是覆盖
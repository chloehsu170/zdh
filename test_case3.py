#-*-coding:utf-8-*-
#邮件等高级应用
__author__ = 'chloe'
import HTMLTestRunner
import unittest
import time,os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
#找到最新测试文件
def sendFile():
    path_dir = "C:\\Python27\\zdh\\report"
    list = os.listdir(path_dir)
    #获取测试文件的修改时间信息并排序，剔除文件夹
    list.sort(key=lambda fn:os.path.getmtime(path_dir+'\\'+fn) if not os.path.isdir(path_dir+'\\'+fn) else 0)
    # newfile = os.path.join(path_dir,list[-1])#拼接文件路径，两种方法
    newfile= path_dir+'\\'+list[-1]
    print(newfile)
    return newfile

#发送测试报告邮件
def sendMail():
    sender = "646567397@qq.com"
    # receiver = "shuangyu170@hotmail.com"
    receiver = "xuyanwen170@gmail.com"
    title = " Python Test Report"
    smtpserver = "smtp.qq.com"
    username = "646567397@qq.com"
    passwd = "ebttbpenicrqbdah"
    with open(sendFile(),"rb") as new_file:#取最新测试报告内容
        newfile = new_file.read()
        print(new_file.mode,new_file.name,new_file.closed)#with内层文件未关闭
    msg = MIMEText(_text=newfile,_subtype="html",_charset="utf-8")#创建邮件实例对象
    msg['Subject'] = Header(title,"utf-8")#邮件主题
    msg['date'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())#设置发送时间

    smtp = smtplib.SMTP_SSL(smtpserver)#取得smtp实例对象
    smtp.connect('smtp.qq.com')#连接smtp服务器
    smtp.login(username,passwd)#登录邮箱
    smtp.sendmail(sender,receiver,msg.as_string())#发送邮件
    smtp.quit()#退出连接
    print("Test report is sent successfully!!")

#自动化执行测试集
def autoTestReport():
    # sys.path.append("//h_unitest//")
    listaa = "C:\\Python27\\zdh\\test_case"
    suite = unittest.defaultTestLoader.discover(start_dir=listaa,pattern="test*.py",top_level_dir=None)

    now = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime())
    with open("report//"+now + "report.html","wb") as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream= fp,
                                           title=u'test report',
                                           description=u'details are as followed:')
        # proc = Process(target=runner.run,args=(i,))
        # proc.start()
        # proc.join()
        runner.run(suite)
    # fp.close() with open as模式写入文件后自动关闭文件，不需要close()
    print("Test report is done now!!")

if __name__ == '__main__':
    # autoTestReport()
    sendMail()

#对方邮箱收不到
#发送的html格式丢失7k文件变1k文件
#主程序，创建测试套件并生成报表，创建报表前先把HTMLTestRunnerNew.py这个文件放在目录下

#创建套件前先导入unittest库
import unittest
import os.path
from lib.HTMLTestRunnerNew import HTMLTestRunner
from common.DynamicPath import testcases_path,reports_path
from common.Handle_email import send_email
# from Class import testcases

suite = unittest.TestSuite()

loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(tesecases))
suite.addTest(loader.discover(testcases_path))

#加载配置测试报告
stream =open(os.path.join(reports_path,'register_Report.html'),'wb')
runner = HTMLTestRunner(stream=stream,
                        title='注册和登录功能自动化报告',
                        description='实现注册、登录接口自动化，注意查看问题',
                        tester='dong')
runner.run(suite)        #运行主程序
stream.close()

send_email(os.path.join(reports_path,'register_Report.html'),'20230226自动化测试报告')


##测试报告另一个模板，先导包

import unittest
import os.path
from lib.HTMLTestRunnerNew import HTMLTestRunner
from common.DynamicPath import testcases_path,reports_path
from common.Handle_email import send_email
from BeautifulReport import BeautifulReport

suite = unittest.TestSuite()

loader = unittest.TestLoader()
suite.addTest(loader.discover(testcases_path))

# 可以将这些代码替换runner和runner.run中的相关代码
br = BeautifulReport(suite)
br.report("自动化接口项目用例",filename="report.html",report_dir=r"D:\untitled\class40\reports")


send_email(os.path.join(reports_path,'register_Report.html'),'20230226自动化测试报告')

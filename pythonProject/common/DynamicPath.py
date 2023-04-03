import os
#获取项目的根目录
basis_path = os.path.dirname(os.path.dirname(__file__))   #__file_表示当前文件的绝对路径,带有文件名

#获取公共模块的路径
comm_path = os.path.join(basis_path,'common')

#获取配置模块的路径
conf_path = os.path.join(basis_path,'conf')

#获取测试数据模块的路径
data_path = os.path.join(basis_path,'data')

#获取库模块的路径
lib_path = os.path.join(basis_path,'lib')

#获取日志模块的路径
log_path = os.path.join(basis_path,'log')

#获取测试报告模块的路径
reports_path = os.path.join(basis_path,'reports')

#获取测试用例模块的路径
testcases_path = os.path.join(basis_path,'testcases')

#获取被测对象模块的路径
objecttest_path = os.path.join(basis_path,'objecttest')
# print(objecttest_path)


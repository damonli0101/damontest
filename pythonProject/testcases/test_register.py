import unittest
import os
import requests
import json
from lib.ddt import ddt,data
from common.ReadExcel import ReadExcel
from common.Handlerlog import log
from common.DynamicPath import data_path
from common.Handleconfig import conf

@ddt
class TestRegister(unittest.TestCase):

    read = ReadExcel(os.path.join(data_path,'testdata.xlsx'),'register')
    datas = read.read_data()

    @data(*datas)
    def test_register(self,case):
        headers = eval(conf.get('api','headers'))  #从配置提取出来时，是字符串，需要转换成字典或去掉字符串引号就是字典了

        #准备数据
        title = (case['title'])
        data = eval(case['testdata'])  #接口输入数据要求为json，所以需要用json.dumps转换一下
        rowid = int(case['caseid'])+1
        excepted = case['excepted']
        url = case['url']
        method = (case['method'])
        print(url,headers)
        #获取实际结果
        if method == 'get' or method == 'GET':
            res = requests.get(url=url,params=data,headers=headers)

        if method == 'post' or method == 'POST':

            res =requests.post(url=url,data=json.dumps(data),headers=headers)

        # print("res = {},type={},excepted ={}".format(res.text,type(res.text),excepted))
        # 断言
        try:
            self.assertEqual(excepted, res.text)   #接口返回的实际结果为json，按文本输出
        except Exception as e:
            log.debug('测试用例[{}]>>>断言失败，预期结果：{}，实际结果：{}'.format(title,excepted, res.text))
            self.read.write_data(row=rowid,column=7,value='fail')
            raise e

        else:
            log.debug('测试用例[{}]>>>断言成功，预期结果：{}，实际结果：{}'.format(title,excepted, res.text))
            self.read.write_data(row=rowid, column=7, value='pass')

if __name__ == "__main__":
    unittest.main()

from configparser import ConfigParser
import os
from common.DynamicPath import conf_path  #从公共模块中调用配置的路径模块


class HandleConfig(ConfigParser):
    def __init__(self, filename):
        # 调用父类的init方法
        super().__init__()
        self.filename = filename
        self.read(filename,encoding="utf8")

    def write_data(self, section, options, value):
        # 写入数据的方法
        self.set(section, options, value)
        # 写完要调用write方法
        self.write(fp=open(self.filename, "w"))


# 因为项目只有一个配置文件，所以直接在这里创建一个对象
conf = HandleConfig(os.path.join(conf_path,"conf.ini"))  #使用os将配置的路径和配置名合并，得到完整的带有配置文件名的路径
'''
使用配置类时，只需要from common.Handleconfig import conf，
即可使用配置类，如conf.get('区域名','配置项名'),conf.wite_data('区域名','配置项名','配置值')
'''
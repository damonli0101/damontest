#封装日志的类
import logging
import os
# from configparser import ConfigParser
from common.Handleconfig import conf
from common.DynamicPath import log_path


class Log:
    @classmethod                        #使用类方法或静态方法都可以，因为不涉及到任何属性
    def create_log(cls):
        # conf = ConfigParser()           #调用cofigparser配置
        # conf.read(os.path.join(conf_path,'conf.ini'))           #使用OS模块，调用地址公共模块，和文件名合并成地址


        mylog = logging.getLogger(conf.get('logging','loggername'))
        mylog.setLevel(conf.get('logging','level'))

        terminal = logging.StreamHandler()
        terminal.setLevel(conf.get('logging','stream_level'))
        mylog.addHandler(terminal)

        filelog = logging.FileHandler(filename= os.path.join(log_path,conf.get('logging','filename')),
                                      encoding='utf8')     #使用地址指定创建日志的位置，
        filelog.setLevel(conf.get('logging','file_level'))
        mylog.addHandler(filelog)

        formats = '%(asctime)s - [%(filename)s -->ling:%(lineno)d] - %(levelname)s: %(message)s'
        fm = logging.Formatter(formats)
        terminal.setFormatter(fm)
        filelog.setFormatter(fm)

        return mylog       #返回方法的结果，也就是收集器（自己命名的mylog)

log =  Log.create_log() # 一个程序只能定义一个日志，否则会重复输出日志文件，没意义
#
#
# # 调试使用
# # mylog = Log.create_log()
# # mylog.info('kkkkkkk')
# # mylog.error('dddddd')
#
# #或者用以下代码
# # class HandlerLog(object):
# #     # 这个函数放在类里面，会不会用到类相关的属性和方法?  其实这个函数和这个类并没有什么关系，就可以定义成一个静态方法
# #     @classmethod
# #     def create_logger(cls):
# #         # 创建一个日志收集器对像,设置日志收集器等级（如没设置，默认是warning等级)
# #         mylog = logging.getLogger("jzr")
# #         mylog.setLevel(level="DEBUG")
# #
# #         # 3 设置日志输出渠道等级,将输出渠道添加到收集器中
# #         sh = logging.StreamHandler()   # 控制台输出
# #         sh.setLevel(level="DEBUG")
# #         mylog.addHandler(sh)
# #
# #         # 创建输出渠道
# #         fh = logging.FileHandler(filename="log6.logs",encoding="utf8")  # 输出到文件
# #         fh.setLevel(level="DEBUG")
# #         mylog.addHandler(fh)
# #
# #         formater = '%(asctime)s - [%(filename)s -->ling:%(lineno)d] - %(levelname)s: %(message)s'
# #
# #         fm = logging.Formatter(formater)
# #         sh.setFormatter(fm)
# #         fh.setFormatter(fm)
# #
# #         return mylog
# #
# # log =  Log.create_log() # 一个程序只能定义一个日志，否则会重复输出日志文件，没意义
#

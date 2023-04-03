
# 封装成类

import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication   # 创建附件的
from email.mime.multipart import MIMEMultipart       # 构造多组件的邮件使用的
from common.Handleconfig import conf

"""
send_email:
    filename  要发送的文件名
    title     邮件主题
    
在这里可以将smtp服务器名称，密码，发件人，收件人的账号等信息放入配置文件中
"""

def send_email(filename,title):
    smtp = smtplib.SMTP_SSL(host=conf.get("email","host"), port=conf.get("email","port"))
    smtp.login(user=conf.get("email","user"), password=conf.get("email","password"))

    # 第二步，构建一封邮件
    msg = MIMEMultipart()  # 创建一封多组件的邮件
    with open(filename, "rb") as f:  # 注意这里用要rb二进制方式打开，否则收到的附件编码内容显示不了中文
        content = f.read()
    # 创建邮件文本内容
    text_msg = MIMEText(content, _subtype="html", _charset="utf8")
    # 添加到多组件的邮件中
    msg.attach(text_msg)

    # 创建邮件的附件 ，有多少个附件，就把这几行代码拷贝几次
    report_file = MIMEApplication(content)
    report_file.add_header('content-disposition', 'attachment', filename=filename)  # filename是的附件名字，其他都是默认值
    msg.attach(report_file)  # 添加附件到邮件中

    msg["Subject"] = title  # 主题,此处不作配置，直接外面输入
    msg["From"] = conf.get("email","from_uesr")  # 发件人
    msg["To"] = conf.get("email","to_user")  # 收件人

    # 第三步，发送邮件
    smtp.send_message(msg, from_addr=conf.get("email","from_uesr"),to_addrs=conf.get("email","to_user").split(','))  # from_addr 发送地址， to_addrs 接收地址

# send_email("report.html","自动化测试报告")
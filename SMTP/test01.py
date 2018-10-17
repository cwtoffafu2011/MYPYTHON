#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '287136142@qq.com'  # 发件人邮箱账号
my_pass = 'olmuslzzekpacbdi'  # 发件人邮箱密码，第三方生成授权码
#my_user = 'wenting.chen@qishon.com'  # 收件人邮箱账号，我这边发送给自己
my_user = '287136142@qq.com'  # 收件人邮箱账号，我这边发送给自己


def mail():
    ret = True
    try:
        msg = MIMEText('这是邮件的主的正文内定：this is a test mail ,from cwt in qs  ,hahahaha   ', 'plain', 'utf-8')
        msg['From'] = formataddr(["昆布", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        #msg['To'] = formataddr(["昆布", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To'] = formataddr(["hello",my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "这是邮件的主题啊！ "  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
#!/usr/bin/python3
import os;
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

#第三方 SMTP  服务
mail_host = "smtp.qq.com"
mail_user = "287136142@qq.com"
mail_pass = "olmuslzzekpacbdi"


#发送方、接收方邮箱地址
sender = "287136142@qq.com"
receivers = "287136142@qq.com"


#创建带附件的实例，发送邮件的内容、及期格式
msg = MIMEMultipart()
msg['From'] = Header('菜鸟带附件的邮件头','utf-8')
msg['To'] = Header('test','utf-8')
subject = '带附件的邮件主题'
msg['Subject'] = Header(subject,'utf-8')

#邮件正文内容
msg.attach(MIMEText('this is a test from cwt multipart mail ','plain','utf-8'))


#构造附件1
att1 =MIMEText(open(os.getcwd()+'\\multipartFile\\test.txt','rb').read(),'base64','utf-8')
att1['Content-Type'] = "application/octet-stream"
att1['Content-Disposition'] = 'attachment;filename="testcwt.txt"'
msg.attach(att1)


#构造附件1
att2 =MIMEText(open(os.getcwd()+'\\multipartFile\\cwt.txt','rb').read(),'base64','utf-8')
att2['Content-Type'] = "application/octet-stream"
att2['Content-Disposition'] = 'attachment;filename="cwt1.txt"'
msg.attach(att2)


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receivers,msg.as_string())
    print("success!")
except smtplib.SMTPException:
    print("error!")
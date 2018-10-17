#!/usr/bin/python3
import os;
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
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
msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header('菜鸟带附件的邮件头','utf-8')
msgRoot['To'] = Header('test','utf-8')
subject = '带附件的邮件主题(for)'
msgRoot['Subject'] = Header(subject,'utf-8')

msgAlternative =  MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

mail_msg = """
<p>Python 邮件发送测试，发送图片。。</p>
<p><a href = "http://220.160.111.78:58003/fbitrad/#/list?type=fabric">面料展示平台web</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
<p><img src="cid:image2"></p>
"""
msgAlternative.attach(MIMEText(mail_msg,'html','utf-8'))

for i in range(1,3):
    #构造附件1
    fp = open(os.getcwd()+"\\imageFile\\testImage0"+str(i)+".jpg",'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<image'+str(i)+'>')
    msgRoot.attach(msgImage)


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receivers,msgRoot.as_string())
    print("success!")
except smtplib.SMTPException:
    print("error!")
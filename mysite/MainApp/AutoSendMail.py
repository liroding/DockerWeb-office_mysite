from sys import argv
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from LoginApp.models import LoginDB  

 
# 第三方 SMTP 服务
mail_host="smtp.126.com"  #设置服务器
mail_user="liroding@126.com"    #用户名
mail_pass="KHZXGJNGBDJRIUFG"   #口令 
 



''' 
sender = "liroding@126.com"
#receivers = ["liroding@126.com","LiroDing@zhaoxin.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
receivers = [_ReceiversMailArg] 
''' 

class MailHandleClass():
    def __init__(self,_SubjectArg,_ContentArg,_FromArg,_ToMesgArg,_ReceiversMailArg):
       self.subject = _SubjectArg
       self.content = _ContentArg
       self.message = MIMEText(self.content, 'plain', 'utf-8')
       self.message['Subject'] = Header(self.subject, 'utf-8')
       self.message['From'] = "liroding<liroding@126.com>"
       self.message['To'] =  _ReceiversMailArg
       #self.message['To'] =  "dingyinglai<dingyinglai@126.com>"
      
       AdminMailArg = "liroding@zhaoxin.com"    
 
       self.sender = "liroding@126.com"
       #receivers = ["liroding@126.com","LiroDing@zhaoxin.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
       self.receivers = [_ReceiversMailArg,AdminMailArg] 
       #print(self.subject) 
    def AutoSendMail(self): 	 

       try:
           smtpObj = smtplib.SMTP()
           smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
          # smtpObj = smtplib.SMTP_SSL(mail_host,465) #for SSL aliyun 
           smtpObj.set_debuglevel(1) 
           smtpObj.login(mail_user,mail_pass)  
           smtpObj.sendmail(self.sender,self.receivers, self.message.as_string())
           smtpObj.close()
           print( "success")
       except smtplib.SMTPException:
           print( "Error: ")
    def GetMailAddr(self,_username):
        print(_username)
        _dictdata = {'mail':'','setting':''}
        detaildatas   = LoginDB.objects.all()
        for a in detaildatas:
            if a.user == _username:
                 _dictdata['mail'] = a.mail
                 _dictdata['setting'] = a.profilesetting
                 return _dictdata
        return 'connot find mail add'
           #print(_tmpdict['mail']) 
#Instance = MailHandleClass("nihao","12","11","34","liroding@zhaoxin.com")
#Instance.AutoSendMail()
#Instance = MailHandleClass("原生态实验室注册成功通知","欢迎您的到来,希望您使用愉快~ "+"\r\n用户:" + "nihao" + "\r\n密码：" + "123456","11","34","liroding@zhaoxin.com")
#Instance = MailHandleClass("原生态实验室注册成功通知","欢迎您的到来,希望您使用愉快~" + "\r\nmimai" + "\r\nnihao","11","34","liroding@zhaoxin.com")
#Instance.AutoSendMail()

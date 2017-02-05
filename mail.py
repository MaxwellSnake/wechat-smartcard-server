#!/usr/bin/python

# from sae.mail import send_mail 
# from sae.mail import EmailMessage
import sae.mail

def sendmail_test():
	m = EmailMessage()
	m.to = '15klli@stu.edu.cn'
	m.subject = 'smartcard test'
	m.html = '<b>this is a test</b>'
	m.smtp = ('smtp.partner.outlook.cn', 587, '15djwang@stu.edu.cn', "wswdjCS6513861", True)
	m.send()

#sae.mail.send_mail('15klli@stu.edu.cn', 'samrtcard test', 'this is a test', 	
#				   ('smtp.partner.outlook.cn', 587, '15djwang@stu.edu.cn', 'wswdjCS6513861',True))

# parm to should be a list []	
def sendEmail(*to):
	if len(to)!=0 :
		sae.mail.send_mail(to, 'smartcard test', 'this is a test', ('smtp.partner.outlook.cn', 587, '15djwang@stu.edu.cn', 'wswdjCS6513861', True))
		return True
	else:
		return False
		
	
if __name__ == '__main__':
	
	to = ['15djwang@stu.edu.cn', '15zxyang@stu.edu.cn', '1905448382@qq.com']
	sendEmail(to)
	
	sendmail_test()
		
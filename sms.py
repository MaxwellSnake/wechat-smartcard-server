#!/usr/local/bin/python
#-*-coding:utf-8-*-

# ！！此文件尾部包含测试代码。你的每一次测试都将耗费1毛钱。

# https访问，需要安装  openssl-devel库。apt-get install openssl-devel

import random #测试用：用于生成随机数验证码

import httplib
import urllib
import json

#服务地址
sms_host = "sms.yunpian.com"
voice_host = "voice.yunpian.com"
#端口号
port = 443
#版本号
version = "v2"
#查账户信息的URI
user_get_uri = "/" + version + "/user/get.json"
#智能匹配模板短信接口的URI
sms_send_uri = "/" + version + "/sms/single_send.json"
#模板短信接口的URI
sms_tpl_send_uri = "/" + version + "/sms/tpl_single_send.json"
#语音短信接口的URI
sms_voice_send_uri = "/" + version + "/voice/send.json"

def get_user_info(apikey):
	"""
	取账户信息
	"""
	conn = httplib.HTTPSConnection(sms_host , port=port)
	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	conn.request('POST',user_get_uri,urllib.urlencode( {'apikey' : apikey}))
	response = conn.getresponse()
	response_str = response.read()
	conn.close()
	return response_str

def send_sms(apikey, text, mobile):
	"""
	通用接口发短信
	"""
	params = urllib.urlencode({'apikey': apikey, 'text': text, 'mobile':mobile})
	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	conn = httplib.HTTPSConnection(sms_host, port=port, timeout=30)
	conn.request("POST", sms_send_uri, params, headers)
	response = conn.getresponse()
	response_str = response.read()
	conn.close()
	return response_str

def tpl_send_sms(apikey, tpl_id, tpl_value, mobile):
	"""
	模板接口发短信
	"""
	params = urllib.urlencode({'apikey': apikey, 'tpl_id':tpl_id, 'tpl_value': urllib.urlencode(tpl_value), 'mobile':mobile})
	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	conn = httplib.HTTPSConnection(sms_host, port=port, timeout=30)
	conn.request("POST", sms_tpl_send_uri, params, headers)
	response = conn.getresponse()
	response_str = response.read()
	conn.close()
	return response_str

# 测试代码部分
if __name__ == '__main__':
	
	apikey = "75420eed3e346f1477f223c43c4a0daf" #修改为您的apikey.可在官网（http://www.yunpian.com)登录后获取
	mobile = "13071679497"  #修改为您要发送的手机号码，多个号码用逗号隔开
	text = "[汕大一卡通]您的验证码为"+str(random.randint(1000,9999)); #修改为您要发送的短信内容
	
	print(get_user_info(apikey)) #查账户信息
	
	#方法1：调用智能匹配模板接口发短信
#	print send_sms(apikey,text,mobile)

	#方法2：调用模板接口发短信（我们使用这个）
	tpl_id = 1702704 #对应的模板内容为：【汕大一卡通】#name#同学，您报失的一卡通#smartcard#已找回，现由#dorm#保管，请本人尽快到#dorm#领取，谢谢！
	tpl_value = {'#name#': '王德杰', '#smartcard#': '2015101065', '#dorm#': '思源宿管处'}
#    print tpl_send_sms(apikey, tpl_id, tpl_value, mobile)

# -*- coding: utf-8 -*-
import hashlib
import web
import lxml
import time
import os
import urllib2, json
import pylibmc  # 以使用 Memcached 功能
from lxml import etree
import check
import control
import models
import re
from user_state import set_user_state, get_user_state, \
    set_user_last_interact_time, get_user_last_interact_time, delete_user_state
from response import wechat_response

class WeixinInterface:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')  # templates 路径——字符串
        self.render = web.template.render(self.templates_root)  # 传入template 路径，渲染（即使用模板）

    def GET(self):
        # 获取输入参数
        data = web.input()
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr

        # 自己的token
        token = "fuckyouass"  # 这里改写为在特定微信公众平台里输入的token

        # 字典序排序
        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        # sha1加密算法        

        # 如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr

    def POST(self):
        # 接收用户的post，并解析提取
        str_xml = web.data()  # 获得post来的数据
        xml = etree.fromstring(str_xml)  # 进行XML解析
        content = xml.find("Content").text  # 获得用户所输入的内容
        msg_type = xml.find("MsgType").text
        user_openid = xml.find("FromUserName").text
        us_openid = xml.find("ToUserName").text

        if msg_type == 'text':
            # 测试封装
            response = wechat_response(user_openid, content)
            return self.render.reply_text(user_openid, us_openid, int(time.time()), response)

        # 数据库测试
        if content == 'test':
            # data = str(time.time())
            data = '123'
            success = models.insert_test(data)
            reply = u'测试完成'
            return self.render.reply_text(user_openid, us_openid, int(time.time()), reply)

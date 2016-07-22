# -*- coding: utf-8 -*-
import hashlib
import web
import lxml
import time
import os
import urllib2,json
from lxml import etree

class WeixinInterface:

    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        #获取输入参数
        data = web.input()
        signature=data.signature
        timestamp=data.timestamp
        nonce=data.nonce
        echostr=data.echostr
        #自己的token
        token="liyou" #这里改写你在微信公众平台里输入的token
        #字典序排序
        list=[token,timestamp,nonce]
        list.sort()
        sha1=hashlib.sha1()
        map(sha1.update,list)
        hashcode=sha1.hexdigest()
        #sha1加密算法        

        #如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr
        
    def POST(self):        
        str_xml = web.data() #获得post来的数据
        xml = etree.fromstring(str_xml)#进行XML解析
        #content=xml.find("Content").text#获得用户所输入的内容
        msgType=xml.find("MsgType").text
        fromUser=xml.find("FromUserName").text
        toUser=xml.find("ToUserName").text
        #return self.render.reply_text(fromUser,toUser,int(time.time()), u"现在的功能可以重复你的消息 ："+content)
        if msgType == 'text':
            content = xml.find("Content").text
            if content == 'help':
            	#replayText = "hello hello hello"
                return self.render.reply_text(fromUser, toUser, int(time.time()), "来输入一个1-4的数字看看有什么惊喜吧")
            if content == '1':
            	#replayText = "hello hello hello"
                return self.render.reply_text(fromUser, toUser, int(time.time()), "球员")
            if content == '2':
            	#replayText = "hello hello hello"
                return self.render.reply_text(fromUser, toUser, int(time.time()), "随便看看")
            if content == '3':
            	#replayText = "hello hello hello"
                return self.render.reply_text(fromUser, toUser, int(time.time()), "天气")
            if content == '4':
            	#replayText = "hello hello hello"
                return self.render.reply_text(fromUser, toUser, int(time.time()), "心情")
            else:
                return self.render.reply_text(fromUser, toUser, int(time.time()), "哎呀出错了 输个help看看正确的调戏方法？")

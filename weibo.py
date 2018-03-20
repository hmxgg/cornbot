# coding=gbk
import time
import urllib.request
import urllib3
import requests
import lxml
from lxml import html
from lxml import etree
import json
import socket
import hashlib
import importlib,sys
import operator
import time, os, sched
import re
importlib.reload(sys)

id = 4215447026742237
def sendMsg(msg):
    par = {'group_id':543392670,'message':msg}
    #par = {'group_id': 672838364, 'message': msg}
    r = requests.get("http://localhost:5700/send_group_msg", params=par)
    djson = ''
    return msg
def weibo():
    par = {'group_id':672838364,'message':''}
    #r = requests.get("https://api.weibo.cn/2/cardlist?networktype=wifi&uicode=10000011&moduleID=708&wb_version=3581&lcardid=23114044f26d34c13530b2132f6c2377d5e7b1__5887697862_-_live&c=android&i=2e79d8a&s=a9af1bb3&ft=0&ua=HUAWEI-HUAWEI%20C199__weibo__8.3.0__android__android4.4.2&wm=2468_1001&aid=01ArEpz8AKXM7gXDydCM9MWNGdxNbTD7mzAqrAYwjhl7hCxMk.&fid=23114044f26d34c13530b2132f6c2377d5e7b1__5887697862_-_live&uid=6501991808&v_f=2&v_p=59&from=1083095010&gsid=_2A253m5QCDeRxGeBL61MY-S_EyzSIHXVS8KDKrDV6PUJbkdAKLWbCkWpNR3TvG1kBl-iREMkUjq_mH4oaOrz-KuPj&imsi=460072002247612&lang=zh_CN&lfid=10080844f26d34c13530b2132f6c2377d5e7b1&page=1&skin=default&count=20&oldwm=2468_1001&sflag=1&containerid=23114044f26d34c13530b2132f6c2377d5e7b1__5887697862_-_live&ignore_inturrpted_error=true&luicode=10000011&need_head_cards=1", params=par)
    r = requests.get("https://m.weibo.cn/api/container/getIndex?display=0&retcode=6102&containerid=1076035887697862", params=par)

    djson = json.loads(r.text)
    global id
 #   print(djson['cards'][0]['card_group'][0]['desc1'])
    index = 0
    if djson['cards'][index]['card_type'] == '11' and '发帖子' in djson['cards'][index]['card_group'][0]['desc'] and id != djson['cards'][index]['card_group'][1]['mblog']['id']:

       # txt = '嘀嘀嘀，更博了！\n熊心瑶：'+djson['data']['cards'][2]['mblog']['text']
       # dr = re.compile(r'<[^>]+>',re.S)
       # dd = dr.sub('',txt)
        print(djson['cards'][index]['card_group'][0])
        dd = '【'
        dd += djson['cards'][index]['card_group'][0]['desc']+'！！！】'
        dd += '\n'+  djson['cards'][index]['card_group'][1]['mblog']['text']
        print(dd)
        sendMsg(dd)
        #print(dd)

schedule = sched.scheduler(time.time, time.sleep)


def perform_command(cmd, inc):
    # 安排inc秒后再次运行自己，即周期运行
    schedule.enter(inc, 0, perform_command, (cmd, inc))

    try:
        weibo()
    except Exception as err:
        print(err)



def timming_exe(cmd, inc=60):
    # enter用来安排某事件的发生时间，从现在起第n秒开始启动
    schedule.enter(inc, 0, perform_command, (cmd, inc))
    # 持续运行，直到计划时间队列变成空为止
    schedule.run()


print("start:")
timming_exe("echo %time%", 2)
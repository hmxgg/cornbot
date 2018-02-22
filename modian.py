# coding=gbk
import time
import urllib.request

import lxml
from lxml import html
from lxml import etree
import websocket
import json
import hashlib
import importlib,sys
import operator
importlib.reload(sys)

url = "https://zhongchou.modian.com/item/10780.html"
pro_id = 10780
def genarate_sign(params):
    d = urllib.parse.urlencode(params)
    d += "&p=das41aq6"
    m2 = hashlib.md5()
    m2.update(d.encode("utf-8"))
    sign = m2.hexdigest()[5:21]
    return sign

def genarate_sign_sorted(d):

    d += "&p=das41aq6"
    m2 = hashlib.md5()
    m2.update(d.encode(encoding='UTF8'))
    sign = m2.hexdigest()[5:21]
    return sign

def orders(proId):
    url = "https://wds.modian.com/api/project/orders"
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = {'page': '1', 'pro_id': proId}
    headers = {'User-Agent': user_agent}
    sign = genarate_sign(values);
    params = {
        'pro_id': proId,
        'page': '1',
        'sign': sign
    };
    p = urllib.parse.urlencode(params).encode(encoding='UTF8')
    req = urllib.request.Request(url, p, headers)
    proxy = urllib.request.ProxyHandler({'http': 'http://118.114.77.473:8080'})
    opener = urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(req, p)
    the_page = response.read().decode("utf-8")
    djson = json.loads(the_page)
    return djson


def jujurank(proId, name):
    url = 'https://wds.modian.com/api/project/rankings'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = {'page': 1, 'pro_id': proId, 'type': 1}
    headers = {'User-Agent': user_agent}
    values = "page=1&pro_id="+str(pro_id)+"&type=1"
    ranksign = genarate_sign_sorted(values)
    params = {'page': 1, 'pro_id': proId, 'sign': ranksign, 'type': 1}
    p = urllib.parse.urlencode(params).encode(encoding='UTF8')
    req = urllib.request.Request(url, p, headers)
    proxy = urllib.request.ProxyHandler({'http': 'http://118.114.77.473:8080'})
    opener = urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(req, p)
    the_page = response.read().decode("utf-8")
    djson = json.loads(the_page)

    return djson


def details(proId):
    url = "https://wds.modian.com/api/project/detail"
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = {'pro_id': proId}
    headers = {'User-Agent': user_agent}
    sign = genarate_sign(values);
    params = {
        'pro_id': proId,
        'sign': sign
    };
    p = urllib.parse.urlencode(params).encode(encoding='UTF8')
    req = urllib.request.Request(url, p, headers)
    proxy = urllib.request.ProxyHandler({'http': 'http://118.114.77.473:8080'})
    opener = urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(req, p)
    the_page = response.read().decode("utf-8")
    djson = json.loads(the_page)
    return djson


last = ""
while 1 == 1:
    datajson = orders(pro_id)
    name = datajson['data'][0]['nickname']
    strs = ""
    money = datajson['data'][0]['backer_money']
    if name == last:
        print("wait");
    else:
        last = str;
        ranklist = jujurank(pro_id,name)['data']
        rank = 0
        for key in ranklist:
            if operator.eq(name,key['nickname']):
                rank = key['rank']
                break
        ws = websocket.create_connection("ws://127.0.0.1:25303")
        strs += name + '刚刚在摩点集了' + str(money) + '元\\n'
        strs += '目前排名：'+ str(rank)
        strs += '\\n感谢这位聚聚对苞谷GNZ48生诞的支持\\n'
        strs += '摩点链接：'+ url
        strs += '\\n目前已集' + str(details(pro_id)['data'][0]['already_raised']) + '元\\n'
        strs += '目标：' + details(pro_id)['data'][0]['goal'] + "元"
        print (strs)
        msg = "{\"act\":\"101\", \"groupid\": \"672838364\", \"msg\": \"" + strs + "\"}"
        ws.send(msg)
        print ("Sent")
        ws.close()
        last = name

    time.sleep(1)



#coding=utf-8
from cqhttp import CQHttp
import hashlib
import urllib
import json
import operator
import requests

pro_id = 10780
def genarate_sign_sorted(d):

    d += "&p=das41aq6"
    m2 = hashlib.md5()
    m2.update(d.encode(encoding='UTF8'))
    sign = m2.hexdigest()[5:21]
    print(sign)
    return sign
def jujurank(proId):
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

def weather_msg(city):
    r = requests.get("https://www.sojson.com/open/api/weather/json.shtml?city="+city).content
    print(r)
    r = json.loads(r)
    msgs = '今天'+city+'天气：'
    msgs += '\n' + str(r['data']['forecast'][1]['type'])
    msgs += '\n温度：' + str(r['data']['wendu'])
    msgs += '\n湿度：'+ str(r['data']['shidu'])
    msgs += '\n'+ str(r['data']['forecast'][1]['high'])
    msgs += '\n' + str(r['data']['forecast'][1]['low'])
    msgs += '\n' + str(r['data']['ganmao'])
    return msgs

bot = CQHttp(api_root='http://127.0.0.1:5700/')


@bot.on_message()
def handle_msg(context):
    print(context)
    msg = ''
    if context['message'] == '集资':
        msg = '摩点链接：https://zhongchou.modian.com/item/10780.html'
    # elif context['message'] == '猴哥':
    #    msg = '真gay!'
    elif context['message'] == '苞谷':
        msg = '人美声甜'

    # elif context['message'] == '思思':
    #     msg = '比小怪兽还可爱！'
    # elif context['message'] == '菠萝':
    #     msg = '最爱发卡卡！'
    # elif context['message'] == '敏敏':
    #     msg = '恩穗老公'
    # elif context['message'] == '文哥':
    #     msg = '最爱发卡卡！'
    # elif context['message'] == '阿淼':
    #     msg = '好高的女饭！'
    # elif context['message'] == 'J聚':
    #     msg = '加拿大金融巨鳄！'
    elif context['message'] == 'yet tiger':
        msg = '虎！火！发！动！'
    elif context['message'] == '广州天气':
        msg = weather_msg('广州')
    elif context['message'] == '重庆天气':
        msg = weather_msg('重庆')
    elif context['message'] == 'rank':
        rankstr = '广州生诞3.0众筹排行榜：\n'
        ranklist = jujurank(10780)['data']
        print(ranklist)
        for key in ranklist:
            rankstr += str(key['rank']) + '：' + key['nickname'] + ', '+ str(key['backer_money'])+ '元' + '\n'
        msg = rankstr
       # print(msg)
    bot.send(context, message=msg, is_raw=True)


@bot.on_event('group_increase')
def handle_group_increase(context):
    bot.send(context, message='欢迎新人～', is_raw=True)  # 发送欢迎新人


@bot.on_request('group', 'friend')
def handle_request(context):
    return {'approve': True}  # 同意所有加群、加好友请求


bot.run(host='127.0.0.1', port=8888)
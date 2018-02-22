#coding=utf-8
from cqhttp import CQHttp

bot = CQHttp(api_root='http://127.0.0.1:5700/',
             access_token='your-token',
             secret='your-secret')


@bot.on_message()
def handle_msg(context):
    bot.send(context, '你好呀，下面一条是你刚刚发的：')
    return {'reply': context['message'], 'at_sender': False}


@bot.on_event('group_increase')
def handle_group_increase(context):
    bot.send(context, message='欢迎新人～', is_raw=True)  # 发送欢迎新人


@bot.on_request('group', 'friend')
def handle_request(context):
    return {'approve': True}  # 同意所有加群、加好友请求


bot.run(host='127.0.0.1', port=8888)
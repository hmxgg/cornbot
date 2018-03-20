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

def sendMsg(msg):
    par = {'group_id':665929187,'message':msg,'auto_escape':False}
    r = requests.get("http://localhost:5700/send_group_msg", params=par)
    djson = ''
    return msg
msg = '[CQ:at,qq=all]'
sendMsg(msg)
#!/usr/bin/env python3
#coding=utf-8
import urllib.request
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import re
import time
import json
import  os

accessKey=['','']


def UpdateDomainRecord(accessKeyId,accessSecret,NewIP):
    client = AcsClient(accessKeyId,accessSecret, 'default')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('alidns.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https') # https | http
    request.set_version('2015-01-09')
    request.set_action_name('UpdateDomainRecord')

    request.add_query_param('RR', 'WWW')
    request.add_query_param('Value', NewIP)
    request.add_query_param('Type', 'A')
    request.add_query_param('RecordId', '17047296276430848')

    response = str(client.do_action(request), encoding = 'utf-8')
    msg=json.loads(response)
    if 'Message' in msg:
        msg = msg['Message']
        content = stamp_to_time() + '  '  + msg + '\n'
        WriteContent('log.conf', content)
    else :
        content = stamp_to_time() + '  ' + 'the ip of demain liuyaoze.cn has change to :'+NewIP + '\n'
        WriteContent('log.conf', content)

def ReadContent(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    return lines[-1]
def WriteContent(file_name,content):
    f = open(file_name,'a+')
    f.write(content)
    f.close()

def GetIP():
    url='http://ip.42.pl/raw'
    get = urllib.request.urlopen(url).read().decode()
    return get

def JudgeIP(newip):
    content=ReadContent('ip.conf')
    ip=re.search('\d+\.\d+\.\d+\.\d+',content)
    if ip != None:
        localip=ip.group()
    else :
        content = stamp_to_time() + '  ' + 'no ip in ip.conf' + '\n'
        WriteContent('log.conf',content)
    if newip!= localip :
        content=stamp_to_time()+'  '+newip+'\n'
        WriteContent('ip.conf',content)
        UpdateDomainRecord(accessKey[0],accessKey[1], newip)

def stamp_to_time():
    timeArray = time.localtime()
    Time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return str(Time)

def socket_conn():
    result=str(os.system('ping -c  1 alidns.aliyuncs.com'))
    if  result !='0':
        content = stamp_to_time() + '  ' + 'fail to connect alidns.aliyuncs.com' + '\n'
        WriteContent('log.conf',content)
    return result

if __name__=='__main__':
    try:
        a=socket_conn()#win上需要屏蔽这两句话。linux上才能用ping -c，故而在linux上需要把JudgeIP(GetIP())这一行再tab一次。
        if a == '0':
			JudgeIP(GetIP())
        #time.sleep(10)
    except Exception as e:
        content = stamp_to_time() + '  ' + e + '\n'
        WriteContent('log.conf',content)
        #time.sleep(10)

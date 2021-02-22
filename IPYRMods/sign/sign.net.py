#! /usr/bin/env python
# -*- coding:utf-8 -*-
import json
import mc
import tool
from System import IO
import time
import datetime
from datetime import date
import thread
data = json.loads(IO.File.ReadAllText('./plugins/sign/data.json'))
item = json.loads(IO.File.ReadAllText('./plugins/sign/item.json'))
def signrespawn(a):
    b = date.today()
    if not data.has_key(str(b.strftime('%Y/%m/%d'))):
        data[str(b.strftime('%Y/%m/%d'))] = {}
    if data[str(b.strftime('%Y/%m/%d'))].has_key(a.playername):
        pass
    else:
        thread.start_new_thread(sendnosign,(GetUUID(a.playername),))

def signinputcommand(a):
    if a.cmd == '/sign':
        thread.start_new_thread(signsign,(a,))    
        return False
                 
def signGetUUID(plname):
    a = json.loads(mc.getOnLinePlayers())
    for key in a:
        if key['playername'] == plname:
            return key['uuid']
    return 'null'

def sendnosign(uuid):
    a = '§3sign§r >>> §4你今天还没有签到哦!§r [§2使用/sign来签到§r]'
    time.sleep(10)
    mc.sendText(uuid,a)
def get_week_day():
    return date.weekday(datetime.datetime.now())

def signsign(a):
    d = date.today()
    if data[str(d.strftime('%Y/%m/%d'))].has_key(a.playername):
        h = '§3sign§r >>> §2你今天签到过了!'
        mc.sendText(GetUUID(a.playername),h)
    else:
        c = date.today()
        now_datetime = datetime.datetime.now(None)
        signtime = now_datetime.strftime('%Y-%m-%d %H:%M:%S')
        data[str(c.strftime('%Y/%m/%d'))][a.playername] = signtime
        tool.WriteAllText('./plugins/sign/data.json',json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
        s = '§3sign§r >>> '+a.playername+' §2今日签到已完成!§r\n§e签到礼包已发放§r\n§3今日签到时间§r >>> '+str(now_datetime.strftime('%H:%M:%S'))+'\n§3今日签到排名§r >> '+str(len(data[str(c.strftime('%Y/%m/%d'))]))
        mc.sendText(GetUUID(a.playername),s)
        mc.addPlayerItem(GetUUID(a.playername),item[get_week_day()]['itemid'],item[get_week_day()]['itemaux'],item[get_week_day()]['count'])
ipyapi.Listen('onInputCommand',signinputcommand)
ipyapi.Listen('onRespawn',signrespawn)
mc.setCommandDescribe('sign','签到')
print '[SIGN] 装载成功！'
print '[SIGN] 作者：Sbaoor'
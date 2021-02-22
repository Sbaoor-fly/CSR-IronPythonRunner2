#! /usr/bin/env python
# -*- coding:utf-8 -*-
import json
import mc
import tool
import thread
import time
from System import IO
ontime = {}
conf = json.loads(IO.File.ReadAllText('./plugins/TimeReward/config.json'))
def online():
    while True:
        time.sleep(60)
        a = mc.getOnLinePlayers()
        if a != '':
            a = json.loads(a)
            for key in a:
                if ontime.has_key(key['playername']):
                    ontime[key['playername']] += 1
                    if ontime[key['playername']] == conf['time']:
                        mc.sendText(TRGetUUID(key['playername']),str(conf['message']).replace('%name%','\"'+str(key['playername'])+'\"').replace('%time%',str(conf['time']/60)).replace('%money%',str(conf['reward_money'])))
                        mc.runcmd('scoreboard players add \"'+str(key['playername'])+'\" money '+str(conf['reward_money']))
                        for kay in conf['runcmd_at_reward']:
                            mc.runcmd(kay.replace('%name%','\"'+str(key['playername'])+'\"'))
                        ontime[key['playername']] = 0
                else:
                    ontime[key['playername']] = 0

def TRGetUUID(plname):
    a = json.loads(mc.getOnLinePlayers())
    for key in a:
        if key['playername'] == plname:
            return key['uuid']
    return 'null'

thread.start_new_thread(online,())
print('在线奖励装载成功')
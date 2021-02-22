#! /usr/bin/env python
# -*- coding:utf-8 -*-
import time
import tool
import thread
import json

def CheckUp(plname,version):
    webget = tool.HttpPost('http://up.qingyimc.cn/home/api/check.php','plugin='+plname)
    if webget != None:
            webget = webget.split('链接',1)
            if  not str(webget[0]).replace('版本：','') == str(version):
                print('[PluginCheck] 插件>>['+plname+']版本不符！云端版本:'+str(webget[0]).replace('版本：','')+',当前版本:'+version)
                print('[PluginCheck] 插件>>['+plname+']下载地址'+webget[1])


def GetUUID(plname):
    a = json.loads(mc.getOnLinePlayers())
    for key in a:
        if key['playername'] == plname:
            return key['uuid']
    return 'null'

def IFOP(plname):
    a = json.loads(IO.File.ReadAllText('permissions.json'))
    xuid = GetXUID(plname)
    for key in a:
        if key['xuid'] == xuid:
            if key['permission'] == 'operator':
                return True
    return False

def GetXUID(plname):
    a = json.loads(mc.getOnLinePlayers())
    for key in a:
        if key['playername'] == plname:
            return key['xuid']
    return 'null'

print '[PluginCheck] 装载成功！'
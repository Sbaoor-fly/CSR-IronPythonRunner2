#! /usr/bin/env python
# -*- coding:utf-8 -*-
# -*- New Mould-*-
# -*- Based on IronPythonRunner2 -*-
from System import IO
import json
import thread
import time
formid = {}
packid = {}
ifuse = {}
if not IO.File.Exists('./plugins/imenu/config.json'):
    IO.Directory.CreateDirectory('./plugins/imenu')
jsons = json.loads(IO.File.ReadAllText('./plugins/imenu/config.json'))
#################
def loadaaaaname(a):
    ifuse[a.playername] = True
##################
def useiiiiiiiitem(a):
    global jsons
    if str(a.itemid) == jsons['itemid']:
        if ifuse[a.playername]:
            thread.start_new_thread(sendform,(a.playername,'main'))
##################################
def formsssssssselect(a):
    formm = json.loads(IO.File.ReadAllText('./plugins/imenu/packs/'+str(packid[a.playername])+'.json'))
    if a.selected != 'null':
        if str(a.formid) == str(formid[a.playername]):
            cmds =  str(formm['buttons'][int(a.selected)]['cmd'][0]['command'])
            if str(formm['buttons'][int(a.selected)]['cmd'][0]['type']) == 'default':
                mc.runcmdAs(GetUUID(a.playername),cmds)
            elif str(formm['buttons'][int(a.selected)]['cmd'][0]['type']) == 'cmd':
                mc.runcmd(cmds.replace('@s','\"'+str(a.playername+'\"')))
            elif str(formm['buttons'][int(a.selected)]['cmd'][0]['type']) == 'opcmd':
                if IFOP(a.playername):
                    mc.runcmdAs(GetUUID(a.playername),cmds)
                else:
                    mc.tellraw('\"'+str(a.playername)+'\"','[§emenu§r] §4你莫得op权限不能执行这个命令')
            elif str(formm['buttons'][int(a.selected)]['cmd'][0]['type']) == 'opform':
                if IFOP(a.playername):
                    thread.start_new_thread(sendform,(a.playername,cmds))
                else:
                    mc.tellraw('\"'+str(a.playername)+'\"','[§emenu§r] §4你莫得op权限不能打开这个表单')           
            elif str(formm['buttons'][int(a.selected)]['cmd'][0]['type']) == 'form':
                thread.start_new_thread(sendform,(a.playername,cmds))
            elif str(formm['buttons'][int(a.selected)]['cmd'][0]['type']) == 'moneycmd':
                if int(GetMoney(GetUUID(a.playername))) > int(formm['buttons'][int(a.selected)]['cmd'][0]['money']):
                    mc.runcmd(cmds.replace('@s','\"'+str(a.playername)+'\"'))
                    RemoveMoney(a.playername,int(formm['buttons'][int(a.selected)]['cmd'][0]['money']))
                else:
                    mc.tellraw('\"'+str(a.playername)+'\"','[§emenu§r] §4你钱不够哦')
##################################
def inpsaqsqwxd(d):
    if d.cmd == '/menu':
        sendform(d.playername,'main')
        return False
##################################
def sendform(name,formpack):
    ifuse[name] = False
    fom = '['
    x = 0
    formm = json.loads(IO.File.ReadAllText('./plugins/imenu/packs/'+str(formpack)+'.json'))
    num = len(formm['buttons'])
    while x < num :
        if x!= 0 :
            fom+=','
        fom +='\''+ (str(formm['buttons'][x]['text']).decode('unicode_escape')) +'\''
        x += 1
    fom += ']'
    packid[name] = formpack
    formid[name] = mc.sendSimpleForm(GetUUID(name),formm['title'],formm['content'],str(fom).replace('\'','\"'))
    time.sleep(1)
    ifuse[name] = True
################################
def GetUUID(plname):
    a = json.loads(mc.getOnLinePlayers())
    for key in a:
        if key['playername'] == plname:
            return key['uuid']
    return 'null'
###########################
def IFOP(plname):
    a = json.loads(IO.File.ReadAllText('permissions.json'))
    for key in a:
        if key['xuid'] == GetXUID(plname):
            if key['permission'] == 'operator':
                return True
    return False
##################################
def RemoveMoney(plname,money):
    mc.runcmd('scoreboard players remove \"'+str(plname)+'\" money '+str(money))
##################################
def GetMoney(pluuid):
    return mc.getscoreboard(str(pluuid),'money')
##################################
def GetXUID(plname):
    a = json.loads(mc.getOnLinePlayers())
    for key in a:
        if key['playername'] == plname:
            return key['xuid']
    return 'null'
##################################
ipyapi.Listen('onUseItem',useiiiiiiiitem)
ipyapi.Listen('onInputCommand',inpsaqsqwxd)
ipyapi.Listen('onLoadName',loadaaaaname)
ipyapi.Listen('onFormSelect',formsssssssselect)
mc.setCommandDescribe('menu','打开菜单')
print('[IMENU] 装载成功')
print('[IMENU] 作者：Sbaoor')
print('[IMENU] 当前版本：2.1.0')
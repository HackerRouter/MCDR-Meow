# -*- coding: utf-8 -*-
from __future__ import division
from urllib.parse import quote

import random
import math


HelpMessage ='''------MCDR Meowv0.1.6-fixed------
一个支持游戏内吸猫猫的插件
§a【格式说明】§r
.help -获取帮助信息
.jrrp -获取今日人品
.draw -抽牌
.afk -提示其他玩家你在挂机
.url -发送一个链接
.welcome set [0/1] -控制入服欢迎开关（默认开启）
.whitelist [add/remove] [PlayerName] -为某人加/减去白名单（须指定人)
.carpet [...] [...] -游戏内设置carpet特性开关（须指定人)
.mpch 获取MCDR Pearl Cannon Helper的帮助信息
--------------------------------'''

MPCHHelpMessage = '''========§6MCDR Pearl Cannon Helper§r========
.mpch 显示这条信息
.mpch calculate [< 珍珠初始速度(m/s) >]  [< 珍珠与TNT角度(>5,<20) >] -珍珠炮射程（单位:m)估算
§6想法提出者&公式贡献者：GhastRs'''

#可恶，哪个大佬能告诉我珍珠初始速度怎么算  ----HackerRouter

welcomerTrue = 1
op = 'HackerRouter'

def on_player_joined(server, playername):
    if welcomerTrue == 1:
      result = 'tellraw @a {"text":"[猫猫] 欢迎' + playername + '加入游戏."}'
      server.execute(str(result))

def work(server, info):
  global welcomerTrue
  finalString = info.content
  if info.is_player == 1:
    if info.content.find('猫') > -1:
      randomText =['喵(つ≧▽≦)つ', '喵喵喵(≧▽≦)', '喵喵喵！', '喵喵喵~~', '喵？喵！']
      result = 'tellraw @a {"text":"[猫猫] ' + random.choice(randomText) + '"}'
      server.execute(str(result))
    elif info.content.find('喵喵') > -1:
      randomText =['喵喵喵！你也是猫猫啊！']
      result = 'tellraw @a {"text":"[猫猫] ' + random.choice(randomText) + '"}'
      server.execute(str(result))
    elif info.content == '.draw ' or info.content == '.draw':
      result = 'tellraw @a {"text":"[猫猫] 未指定牌堆名."}'
      server.execute(str(result))
    elif info.content == '.draw 塔罗牌' or info.content == '.draw 大阿卡那':
      randomText =['【0】愚者', '【1】魔术师', '【2】女祭司', '【3】女皇', '【4】皇帝', '【5】教皇', '【6】恋人', '【7】战车', '【8】力量', '【9】隐者', '【10】命运之轮', '【11】正义', '【12】倒吊人', '【13】死神', '【14】节制', '【15】恶魔', '【16】塔', '【17】星星', '【18】月亮', '【19】太阳', '【20】审判', '【21】世界']
      result = 'tellraw @a {"text":"[猫猫] ' + info.player + '抽到的是: ' + random.choice(randomText) + '"}'
      server.execute(str(result))
    elif info.content == '.draw 小阿卡那':
      randomText =['权杖', '星币', '圣杯', '宝剑']
      result = 'tellraw @a {"text":"[猫猫] ' + info.player + '抽到的是: ' + random.choice(randomText) + '"}'
      server.execute(str(result))
    elif info.content.startswith('.jrrp'):
      result = str(random.randint(1,100))
      server.execute(str('tellraw @a {"text":"[猫猫] ' + info.player + '今天的人品值是: ' + result + '"}'))
    elif info.content.startswith('.welcome set '):
      welcomerTrue = info.content[13:]
      try:
         welcomerTrue = int(welcomerTrue)
         if welcomerTrue == 1:
           server.execute(str('tellraw @a {"text":"[猫猫] 已将欢迎提示设为开启."}'))
         elif welcomerTrue == 0:
           server.execute(str('tellraw @a {"text":"[猫猫] 已将欢迎提示设为关闭."}'))
         else:
           server.execute(str('tellraw @a {"text":"[猫猫] 错误,非法数据，仅可输入0或1."}'))
      except:
           server.execute(str('tellraw @a {"text":"[猫猫] 错误,非法数据，必须为整数."}'))
    elif info.content.startswith('.url '):
    	result = info.content[5:]
    	server.execute(str('tellraw @a [{"text":"<' + info.player + '> "},{"text":"' + result + '","color":"blue","underlined":"true","clickEvent":{"action":"open_url","value":"' + result + '"}}]'))
    elif info.content == '.afk':
    	server.execute(str('tellraw @a {"text":"' + info.player + ' is afk-ing."}'))
    elif info.content.startswith('.whitelist add ') and info.player == op:
    	result = info.content[15:]
    	server.execute(str('whitelist add ' + result))
    elif info.content.startswith('.whitelist remove ') and info.player == op:
    	result = info.content[18:]
    	server.execute(str('whitelist remove ' + result))
    elif info.content.startswith('.carpet ') and info.player == op:
    	result = info.content[8:]
    	server.execute(str('carpet ' + result))
    elif info.content.find('大佬') > -1 and int(finalString.find('tamakoooo')) > -1:
    	server.execute(str('kick ' + info.player +' ...'))
    	server.tell('Planetes_','{"text":"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"}')

    elif info.content.startswith('.mpch'):
      if info.content.startswith('.mpch calculate'):
        pearlSpeed = int(info.content.split()[2])
        angle = math.ceil(float(info.content.split()[3]))
        finalValue = str(pearlSpeed * 100 * ( angle/100 + 1 ))
        server.say('MPCH的计算结果：' + finalValue + 'm.')
      else:
        server.say(MPCHHelpMessage)
    elif info.content.startswith('.help'):
      server.say(HelpMessage)

# MCDaemon
def onServerInfo(server, info):
	if info.isPlayer == 1:
		work(server, info)


# MCDReforged
def on_info(server, info):
	if info.is_player:
		work(server, info)


def on_load(server, old):
	server.add_help_message('.help', '多功能的聊天机器人')
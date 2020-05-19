# -*- coding: utf-8 -*-
from __future__ import division
from urllib.parse import quote
import random


HelpMessage ='''------MCDR Meowv0.1-fixed------
一个支持游戏内吸猫猫的插件
§a【格式说明】§r
.help -获取帮助信息
.jrrp -获取今日人品
.draw -抽牌
.welcome set [0/1] -控制入服欢迎开关（默认开启）
--------------------------------'''

welcomerTrue = 1


def on_player_joined(server, playername):
    if welcomerTrue == 1:
      result = 'tellraw @a {"text":"[猫猫] 欢迎' + playername + '加入游戏."}'
      server.execute(str(result))

def work(server, info):
  global welcomerTrue
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
	server.add_help_message('.help', '享受猫猫给你带来的乐趣')
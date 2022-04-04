import json
import os
import requests,random,os,json, re, filetype,datetime
from .paiziconfig import *
import hoshino
from nonebot import on_command
from hoshino.typing import MessageSegment
from hoshino import R, Service, util
import time
sv = Service('查牌子', enable_on_default=False)

def get_paizi(uid):   
    result = requests.get(f'https://api.live.bilibili.com/xlive/web-ucenter/user/MedalWall?target_id={uid}', headers=headers)
    data_json = result.json()
    first_line = '粉丝牌：\n'
    medal_wall = str()
    num = 10 if len(data_json['data']['list']) > 10 else len(data_json['data']['list'])
    for i in range(num):
        medal_wall = medal_wall + data_json['data']['list'][i]['medal_info']['medal_name'] + str(
            data_json['data']['list'][i]['medal_info']['level']) + '级' + '\t{}\n'.format(
            data_json['data']['list'][i]['target_name'])
    guidang(uid)
    return first_line + medal_wall[:-1]


def guidang(uid):
    with open(os.path.join(os.path.dirname(__file__), 'LB.json'),"r",encoding='utf-8') as dump_f:
        words = json.load(dump_f)
    today = datetime.datetime.today().__format__('%Y-%m-%d-%H:%M:%S')
    time = 1
    if (uid in words):
        time = int(f'{words[uid]["time"]}') + 1
    words[uid] = {"Buid":uid,"daytime":today,"time":time}
    with open(os.path.join(os.path.dirname(__file__), 'LB.json'),'w',encoding='utf8') as f:
        json.dump(words, f, ensure_ascii=False,indent=2)

@sv.on_prefix('查牌子')
async def chapaizi(bot,ev):
    uid = ev.message.extract_plain_text().strip()
    a = chaxun(uid)
    if a==1:
        with open(os.path.join(os.path.dirname(__file__), 'LB.json'),"r",encoding='utf-8') as dump_f:
            cha = json.load(dump_f)
            lasttime = f'{cha[uid]["daytime"]}'
            cishu = f'{cha[uid]["time"]}'
            print (lasttime)
        await bot.send(ev, '注意！\n'+uid+'已经于'+lasttime+'查询过了'+cishu+'次', at_sender=True)
        await bot.send(ev, get_paizi(uid), at_sender=True)
    else:
        await bot.send(ev, get_paizi(uid), at_sender=True)
def chaxun(uid):
    with open(os.path.join(os.path.dirname(__file__), 'LB.json'),"r",encoding='utf-8') as dump_f:
        cha = json.load(dump_f)
    if (uid in cha):
        return 1
    return 2

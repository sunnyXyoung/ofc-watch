import asyncio
import requests
import time
import os
from dotenv import load_dotenv
import sys
import json
import logging
import discord
import datetime
load_dotenv()

board_to_channel = {
    'money': '金錢追蹤',
    'fight_exp': '戰熟追蹤',
    'mine_exp': '礦熟追蹤',
    'forge_exp': '鍛熟追蹤',
    "role2": '副職追蹤',
}

channel_to_board = {
    '金錢追蹤': 'money',
    '戰熟追蹤': 'fight_exp',
    '礦熟追蹤': 'mine_exp',
    '鍛熟追蹤': 'forge_exp',
    '副職追蹤': 'role2',
}

nl_dict = {
    'money': '元',
    'fight_exp': '點戰熟',
    'mine_exp': '點礦熟',
    'forge_exp': '點鍛熟'
}

nl_dict2 = {
    'money': '金錢',
    'fight_exp': '戰熟',
    'mine_exp': '礦熟',
    'forge_exp': '鍛熟',

}

topic_to_stat = {
    'money': 'money',
    'fight_exp': 'fightExp',
    'mine_exp': 'mineExp',
    'forge_exp': 'forgeExp',
}

logging.basicConfig(level=logging.NOTSET)


def sec_to_text(sec):
    if sec>60:
        if int(int(sec/60)/60) == 0:
            return f' {int(sec-int(int(sec/60)/60))//60 +1} 分鐘'
        else:
            return f' {int(int(sec/60)/60)} 小時 {int(int(sec-int(int(sec/60)/60)*3600)//60 +1)} 分鐘'
    else:
        return f' {int(sec)+1} 秒'


async def update_leaderboard():
    
    leaderboards = ['money', 'fight_exp', 'forge_exp', 'mine_exp', 'kill']
    headers = {
        'User-Agent': 'I just wanna know all the secret data',
        'Accept': '*/*',
        'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Origin': 'https://ourfloatingcastle.com',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }
    now_leaderboard_dict = {}
    error_count = 0
    for i in leaderboards:
        while True:
            response = requests.get(f'https://api.ourfloatingcastle.com/api/users?order={i}', headers=headers)
            if response.status_code != 200:
                error_count += 1
                if error_count > 10:
                    logging.error(response, 'over 10 errors')
                    exit()
            else:
                break

        now_leaderboard_dict[i] = json.loads(response.text)['players']
        print(now_leaderboard_dict[i])

    return now_leaderboard_dict

client = discord.Client()

# log = open(os.path.join(webroot, 'ofc', f'{round}.leaderboard'), 'a', encoding="utf-8")


@client.event
async def on_ready():
    print(f'{client.user} online')
    for g in client.guilds:
        if g.id == 678210712824315924:
            break


    prev_leaderboard = eval("{510: {'id': 510, 'nickname': '沙優的狗', 'color': '#b78830', 'role': '鍛造師', 'role2': '效率王', 'factionName': '月餅', 'money': 250002, 'fightExp': 0, 'forgeExp': 49370, 'mineExp': 5, 'board': ['money', 'forge_exp']}, 13: {'id': 13, 'nickname': '草薙寧寧', 'color': '#b78830', 'role': '鍛造師', 'role2': '效率王', 'factionName': '月餅', 'money': 230029, 'fightExp': 0, 'forgeExp': 20930, 'mineExp': 0, 'board': ['money', 'forge_exp']}, 288: {'id': 288, 'nickname': 'kc', 'color': '#a6bf70', 'role': '鍛造師', 'role2': '礦裝師', 'factionName': '文旦', 'money': 214270, 'fightExp': 0, 'forgeExp': 13487, 'mineExp': 12, 'board': ['money', 'forge_exp']}, 1159: {'id': 1159, 'nickname': '劉世偉', 'color': '#b78830', 'role': '鍛造師', 'role2': '效率王', 'factionName': '月餅', 'money': 152980, 'fightExp': 11, 'forgeExp': 12658, 'mineExp': 0, 'board': ['money', 'forge_exp']}, 207: {'id': 207, 'nickname': '舔耳喵', 'color': '#b78830', 'role': '礦工', 'role2': '蟑螂', 'factionName': '月餅', 'money': 150000, 'fightExp': 1309, 'forgeExp': 136, 'mineExp': 297, 'board': ['money']}, 180: {'id': 180, 'nickname': '墨子鍛造師', 'color': '#a7604b', 'role': '鍛造師', 'role2': '效率王', 'factionName': '烤肉', 'money': 147027, 'fightExp': 0, 'forgeExp': 40435, 'mineExp': 12, 'board': ['money', 'forge_exp']}, 90: {'id': 90, 'nickname': '新月', 'color': '#a7604b', 'role': '鍛造師', 'role2': '效率王', 'factionName': '烤肉', 'money': 145235, 'fightExp': 0, 'forgeExp': 42688, 'mineExp': 4, 'board': ['money', 'forge_exp']}, 666: {'id': 666, 'nickname': '德克教教皇天雲絲', 'color': '#b78830', 'role': '鍛造師', 'role2': '效率王', 'factionName': '月餅', 'money': 132700, 'fightExp': 1, 'forgeExp': 41574, 'mineExp': 55, 'board': ['money', 'forge_exp']}, 42: {'id': 42, 'nickname': '蜂蜜史萊姆', 'color': '#a7604b', 'role': '鍛造師', 'role2': '效率王', 'factionName': '烤肉', 'money': 114015, 'fightExp': 0, 'forgeExp': 31445, 'mineExp': 49, 'board': ['money', 'forge_exp']}, 10: {'id': 10, 'nickname': 'ST', 'color': '#b78830', 'role': '鍛造師', 'role2': '效率王', 'factionName': '月餅', 'money': 97114, 'fightExp': 5, 'forgeExp': 29442, 'mineExp': 10, 'board': ['money', 'forge_exp']}, 472: {'id': 472, 'nickname': '魔山教主', 'color': '#a7604b', 'role': '鍛造師', 'role2': '效率王', 'factionName': '烤肉', 'money': 91556, 'fightExp': 0, 'forgeExp': 4100, 'mineExp': 139, 'board': ['money']}, 618: {'id': 618, 'nickname': '點點', 'color': '#b78830', 'role': '鍛造師', 'role2': '效率王', 'factionName': '月餅', 'money': 90015, 'fightExp': 7, 'forgeExp': 27875, 'mineExp': 0, 'board': ['money', 'forge_exp']}, 1: {'id': 1, 'nickname': '吳剛', 'color': '#a6bf70', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '文旦', 'money': 61813, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 15478, 'badge': {'color': 'blue', 'borderColor': 'cyan.700', 'label': '茅場'}, 'board': ['money', 'mine_exp']}, 867: {'id': 867, 'nickname': '雪', 'color': '#a6bf70', 'role': '鍛造師', 'role2': '礦裝師', 'factionName': '文旦', 'money': 61369, 'fightExp': 0, 'forgeExp': 5160, 'mineExp': 16, 'board': ['money']}, 165: {'id': 165, 'nickname': '人性本惡', 'color': '#a7604b', 'role': '戰鬥員', 'role2': '斥候', 'factionName': '烤肉', 'money': 57236, 'fightExp': 8518, 'forgeExp': 0, 'mineExp': 65, 'kill': 50, 'killed': 11, 'board': ['money', 'fight_exp']}, 250: {'id': 250, 'nickname': '夕洛', 'color': '#a7604b', 'role': '鍛造師', 'role2': '效率王', 'factionName': '烤肉', 'money': 52448, 'fightExp': 9, 'forgeExp': 13078, 'mineExp': 0, 'board': ['money', 'forge_exp']}, 200: {'id': 200, 'nickname': '野格肉粽', 'color': '#a6bf70', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '文旦', 'money': 48295, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 3777, 'board': ['money', 'mine_exp']}, 8: {'id': 8, 'nickname': '餓了', 'color': '#a7604b', 'role': '礦工', 'factionName': '烤肉', 'money': 44646, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 2816, 'board': ['money']}, 963: {'id': 963, 'nickname': '奶酪', 'color': '#a7604b', 'role': '戰鬥員', 'role2': '長槍使', 'factionName': '烤肉', 'money': 43658, 'fightExp': 1895, 'forgeExp': 0, 'mineExp': 59, 'board': ['money']}, 21: {'id': 21, 'nickname': '翼', 'color': '#a7604b', 'role': '鍛造師', 'role2': '礦裝師', 'factionName': '烤肉', 'money': 41963, 'fightExp': 0, 'forgeExp': 7381, 'mineExp': 22, 'board': ['money']}, 404: {'id': 404, 'nickname': 'Kaori', 'color': '#a6bf70', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '文旦', 'money': 38168, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 3115, 'board': ['money']}, 392: {'id': 392, 'nickname': '楊坤', 'color': '#a7604b', 'role': '戰 鬥員', 'factionName': '烤肉', 'money': 37179, 'fightExp': 2588, 'forgeExp': 0, 'mineExp': 55, 'board': ['money']}, 12: {'id': 12, 'nickname': '蒼月舜臨', 'color': '#a7604b', 'role': '鍛造師', 'role2': '效率王', 'factionName': '烤肉', 'money': 37174, 'fightExp': 0, 'forgeExp': 5170, 'mineExp': 20, 'board': ['money']}, 116: {'id': 116, 'nickname': '月球戰鬥仙女 嫦娥', 'color': '#b78830', 'role': '戰鬥員', 'factionName': '月餅', 'money': 35489, 'fightExp': 1752, 'forgeExp': 0, 'mineExp': 0, 'board': ['money']}, 457: {'id': 457, 'nickname': '天籁唱将', 'color': '#a7604b', 'role': '鍛造師', 'role2': '效率王', 'factionName': '烤肉', 'money': 35193, 'fightExp': 0, 'forgeExp': 8813, 'mineExp': 41, 'board': ['money', 'forge_exp']}, 1488: {'id': 1488, 'nickname': '九尾院ルリ', 'color': '#a7604b', 'role': '鍛造師', 'role2': '效率王', 'factionName': '烤肉', 'money': 34953, 'fightExp': 0, 'forgeExp': 5091, 'mineExp': 1, 'board': ['money']}, 771: {'id': 771, 'nickname': '幻影寒冰', 'color': '#a7604b', 'role': '鍛造師', 'role2': '效率王', 'factionName': '烤肉', 'money': 32323, 'fightExp': 3, 'forgeExp': 7629, 'mineExp': 24, 'board': ['money']}, 5: {'id': 5, 'nickname': '魔法少女無名', 'color': '#a7604b', 'role': '鍛造師', 'role2': '效率王', 'factionName': '烤肉', 'money': 30779, 'fightExp': 36, 'forgeExp': 8579, 'mineExp': 0, 'board': ['money']}, 1473: {'id': 1473, 'nickname': '好吃點點', 'color': '#b78830', 'role': '礦工', 'factionName': '月餅', 'money': 30000, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 6, 'board': ['money']}, 106: {'id': 106, 'nickname': 'SCP', 'color': '#a7604b', 'role': '礦工', 'factionName': '烤肉', 'money': 27118, 'fightExp': 0, 'forgeExp': 11, 'mineExp': 1565, 'board': ['money']}, 668: {'id': 668, 'nickname': '克萊因', 'color': '#b78830', 'role': '戰鬥員', 'role2': '衛兵', 'factionName': '月餅', 'money': 430, 'fightExp': 18409, 'forgeExp': 0, 'mineExp': 50, 'kill': 21, 'killed': 2, 'board': ['fight_exp']}, 34: {'id': 34, 'nickname': '有紀', 'color': '#a7604b', 'role': '戰鬥員', 'role2': '衛兵', 'factionName': '烤肉', 'money': 8394, 'fightExp': 17463, 'forgeExp': 0, 'mineExp': 15, 'kill': 197, 'killed': 11, 'board': ['fight_exp']}, 32: {'id': 32, 'nickname': '白銀騎士黑貓', 'color': '#b78830', 'role': '戰鬥員', 'role2': '衛兵', 'factionName': '月餅', 'money': 89, 'fightExp': 12401, 'forgeExp': 0, 'mineExp': 1970, 'kill': 166, 'killed': 5, 'board': ['fight_exp']}, 243: {'id': 243, 'nickname': '三司あやせ', 'color': '#a6bf70', 'role': '戰鬥員', 'role2': '蟑螂', 'factionName': '文旦', 'money': 2135, 'fightExp': 10514, 'forgeExp': 0, 'mineExp': 45, 'kill': 109, 'killed': 35, 'board': ['fight_exp']}, 161: {'id': 161, 'nickname': '桐谷和人8', 'color': '#a7604b', 'role': '戰鬥員', 'role2': '衛兵', 'factionName': '烤肉', 'money': 202, 'fightExp': 8134, 'forgeExp': 0, 'mineExp': 12, 'kill': 15, 'killed': 20, 'board': ['fight_exp']}, 242: {'id': 242, 'nickname': '軍事機密', 'color': '#a6bf70', 'role': '戰鬥員', 'role2': '衛兵', 'factionName': '文旦', 'money': 26, 'fightExp': 6469, 'forgeExp': 0, 'mineExp': 47, 'kill': 58, 'killed': 33, 'board': ['fight_exp']}, 312: {'id': 312, 'nickname': 'STF5', 'color': '#b78830', 'role': '戰鬥員', 'role2': '斥候', 'factionName': '月餅', 'money': 245, 'fightExp': 5570, 'forgeExp': 0, 'mineExp': 45, 'board': ['fight_exp']}, 521: {'id': 521, 'nickname': '胡桃', 'color': '#b78830', 'role': '戰鬥員', 'role2': '衛兵', 'factionName': '月餅', 'money': 0, 'fightExp': 5262, 'forgeExp': 0, 'mineExp': 30, 'kill': 71, 'killed': 0, 'board': ['fight_exp']}, 350: {'id': 350, 'nickname': '沙優劍士', 'color': '#a7604b', 'role': '戰鬥員', 'role2': '衛兵', 'factionName': '烤肉', 'money': 1995, 'fightExp': 4824, 'forgeExp': 0, 'mineExp': 57, 'board': ['fight_exp']}, 76: {'id': 76, 'nickname': '三玖天下第一', 'color': '#a7604b', 'role': '戰鬥員', 'role2': '衛兵', 'factionName': '烤肉', 'money': 1857, 'fightExp': 4712, 'forgeExp': 0, 'mineExp': 0, 'kill': 8, 'killed': 8, 'board': ['fight_exp']}, 974: {'id': 974, 'nickname': 'kc13', 'color': '#a6bf70', 'role': '戰鬥員', 'role2': '衛兵', 'factionName': '文旦', 'money': 4114, 'fightExp': 4565, 'forgeExp': 0, 'mineExp': 30, 'kill': 93, 'killed': 29, 'board': ['fight_exp']}, 633: {'id': 633, 'nickname': '我是小帳四號', 'color': '#b78830', 'role': '戰鬥員', 'role2': '衛兵', 'factionName': '月餅', 'money': 8254, 'fightExp': 4394, 'forgeExp': 0, 'mineExp': 15, 'kill': 72, 'killed': 13, 'board': ['fight_exp']}, 817: {'id': 817, 'nickname': '德克教第一支部教徒絲絲', 'color': '#b78830', 'role': '戰鬥員', 'role2': '衛兵', 'factionName': '月餅', 'money': 1509, 'fightExp': 4343, 'forgeExp': 0, 'mineExp': 0, 'kill': 193, 'killed': 25, 'board': ['fight_exp']}, 538: {'id': 538, 'nickname': '貓咪奶奶', 'color': '#a7604b', 'role': '戰鬥員', 'role2': '長槍使', 'factionName': ' 烤肉', 'money': 904, 'fightExp': 4043, 'forgeExp': 0, 'mineExp': 55, 'board': ['fight_exp']}, 196: {'id': 196, 'nickname': '荀子戰士', 'color': '#a7604b', 'role': '戰鬥員', 'role2': '斥候', 'factionName': '烤 肉', 'money': 1574, 'fightExp': 3889, 'forgeExp': 0, 'mineExp': 80, 'board': ['fight_exp']}, 49: {'id': 49, 'nickname': '德克薩斯做得到嗎', 'color': '#b78830', 'role': '戰鬥員', 'role2': '衛兵', 'factionName': '月餅', 'money': 2139, 'fightExp': 3794, 'forgeExp': 0, 'mineExp': 130, 'kill': 14, 'killed': 20, 'board': ['fight_exp']}, 29: {'id': 29, 'nickname': '寧寧ロボ', 'color': '#b78830', 'role': '戰鬥員', 'role2': '斥候', 'factionName': '月餅', 'money': 3710, 'fightExp': 3562, 'forgeExp': 0, 'mineExp': 80, 'kill': 52, 'killed': 4, 'board': ['fight_exp']}, 381: {'id': 381, 'nickname': '空白3', 'color': '#a7604b', 'role': '戰鬥員', 'role2': '斥候', 'factionName': '烤肉', 'money': 1893, 'fightExp': 3499, 'forgeExp': 6, 'mineExp': 14, 'board': ['fight_exp']}, 706: {'id': 706, 'nickname': '一家烤肉萬家燒', 'color': '#a7604b', 'role': '戰鬥員', 'role2': '長槍使', 'factionName': '烤肉', 'money': 10829, 'fightExp': 3475, 'forgeExp': 0, 'mineExp': 77, 'board': ['fight_exp']}, 321: {'id': 321, 'nickname': '雲鯉丸', 'color': '#a7604b', 'role': '戰鬥員', 'role2': '衛兵', 'factionName': '烤肉', 'money': 9294, 'fightExp': 3422, 'forgeExp': 0, 'mineExp': 50, 'board': ['fight_exp']}, 170: {'id': 170, 'nickname': '傑哥不要啊啊', 'color': '#a7604b', 'role': '戰鬥員', 'role2': '斥候', 'factionName': '烤肉', 'money': 1996, 'fightExp': 3420, 'forgeExp': 0, 'mineExp': 0, 'kill': 9, 'killed': 18, 'board': ['fight_exp']}, 579: {'id': 579, 'nickname': 'SickDown', 'color': '#a7604b', 'role': '戰鬥員', 'role2': '斥候', 'factionName': '烤肉', 'money': 404, 'fightExp': 3383, 'forgeExp': 0, 'mineExp': 15, 'kill': 9, 'killed': 15, 'board': ['fight_exp']}, 906: {'id': 906, 'nickname': '休閒雲玩家', 'color': '#a6bf70', 'role': '戰鬥員', 'role2': '斥候', 'factionName': '文旦', 'money': 796, 'fightExp': 3262, 'forgeExp': 0, 'mineExp': 50, 'kill': 8, 'killed': 15, 'board': ['fight_exp']}, 14: {'id': 14, 'nickname': '冒險雷包', 'color': '#a7604b', 'role': '戰鬥員', 'factionName': '烤肉', 'money': 4892, 'fightExp': 3052, 'forgeExp': 0, 'mineExp': 60, 'board': ['fight_exp']}, 187: {'id': 187, 'nickname': '櫻之詩', 'color': '#a6bf70', 'role': '戰鬥員', 'factionName': '文旦', 'money': 1335, 'fightExp': 3008, 'forgeExp': 0, 'mineExp': 100, 'board': ['fight_exp']}, 673: {'id': 673, 'nickname': '我只 是個路過的卡面賴打', 'color': '#b78830', 'role': '戰鬥員', 'role2': '斥候', 'factionName': '月餅', 'money': 12692, 'fightExp': 3000, 'forgeExp': 0, 'mineExp': 58, 'kill': 16, 'killed': 4, 'board': ['fight_exp']}, 279: {'id': 279, 'nickname': 'Uru唏', 'color': '#a7604b', 'role': '戰鬥員', 'role2': '衛兵', 'factionName': '烤肉', 'money': 17000, 'fightExp': 2941, 'forgeExp': 0, 'mineExp': 204, 'board': ['fight_exp']}, 523: {'id': 523, 'nickname': '吳亮德', 'color': '#b78830', 'role': '戰鬥員', 'role2': '斥候', 'factionName': '月餅', 'money': 10, 'fightExp': 2912, 'forgeExp': 0, 'mineExp': 38, 'board': ['fight_exp']}, 1022: {'id': 1022, 'nickname': '桐谷和人12', 'color': '#a7604b', 'role': '戰鬥員', 'role2': '長槍使', 'factionName': '烤肉', 'money': 2021, 'fightExp': 2877, 'forgeExp': 0, 'mineExp': 16, 'board': ['fight_exp']}, 112: {'id': 112, 'nickname': '不是白學', 'color': '#a6bf70', 'role': '鍛造師', 'role2': '效率王', 'factionName': '文旦', 'money': 8714, 'fightExp': 13, 'forgeExp': 36706, 'mineExp': 150, 'board': ['forge_exp']}, 159: {'id': 159, 'nickname': '雷姆', 'color': '#a7604b', 'role': '鍛造師', 'role2': '效率王', 'factionName': '烤肉', 'money': 4105, 'fightExp': 60, 'forgeExp': 18659, 'mineExp': 1, 'board': ['forge_exp']}, 1168: {'id': 1168, 'nickname': '可愛的霧之幻想', 'color': '#b78830', 'role': '鍛造師', 'role2': '效率王', 'factionName': '月餅', 'money': 81, 'fightExp': 226, 'forgeExp': 18532, 'mineExp': 8, 'board': ['forge_exp']}, 1304: {'id': 1304, 'nickname': '好運蘿莉', 'color': '#a7604b', 'role': '鍛造師', 'role2': '效率王', 'factionName': '烤肉', 'money': 47, 'fightExp': 1, 'forgeExp': 18337, 'mineExp': 0, 'board': ['forge_exp']}, 398: {'id': 398, 'nickname': '霧の幻想 なベール', 'color': '#a6bf70', 'role': '鍛造師', 'role2': '效率王', 'factionName': '文旦', 'money': 22705, 'fightExp': 2, 'forgeExp': 18001, 'mineExp': 0, 'board': ['forge_exp']}, 26: {'id': 26, 'nickname': '桐谷和人', 'color': '#a7604b', 'role': '鍛造師', 'role2': '效率王', 'factionName': '烤肉', 'money': 14540, 'fightExp': 4, 'forgeExp': 14794, 'mineExp': 0, 'badge': {'color': 'red', 'borderColor': 'red.600', 'label': '起司幫'}, 'board': ['forge_exp']}, 39: {'id': 39, 'nickname': '黑貓鍛造不能睡覺', 'color': '#b78830', 'role': '鍛造師', 'role2': '效率王', 'factionName': ' 月餅', 'money': 11313, 'fightExp': 0, 'forgeExp': 14037, 'mineExp': 5, 'board': ['forge_exp']}, 313: {'id': 313, 'nickname': '沙優', 'color': '#a7604b', 'role': '鍛造師', 'role2': '效率王', 'factionName': '烤 肉', 'money': 19007, 'fightExp': 0, 'forgeExp': 13899, 'mineExp': 12, 'board': ['forge_exp']}, 1065: {'id': 1065, 'nickname': '不二家的笑容沒季家的甜', 'color': '#b78830', 'role': '鍛造師', 'role2': '效率王', 'factionName': '月餅', 'money': 19386, 'fightExp': 0, 'forgeExp': 13418, 'mineExp': 9, 'board': ['forge_exp']}, 722: {'id': 722, 'nickname': '放空', 'color': '#a6bf70', 'role': '鍛造師', 'role2': '效率王', 'factionName': '文旦', 'money': 8026, 'fightExp': 2, 'forgeExp': 12776, 'mineExp': 1, 'board': ['forge_exp']}, 805: {'id': 805, 'nickname': '香雞牌', 'color': '#a7604b', 'role': '鍛造師', 'role2': '效率王', 'factionName': '烤肉', 'money': 22892, 'fightExp': 150, 'forgeExp': 12390, 'mineExp': 50, 'board': ['forge_exp']}, 932: {'id': 932, 'nickname': '鐵人', 'color': '#a7604b', 'role': '鍛造師', 'role2': '效率王', 'factionName': '烤肉', 'money': 26598, 'fightExp': 10, 'forgeExp': 11038, 'mineExp': 0, 'board': ['forge_exp']}, 33: {'id': 33, 'nickname': '重擊', 'color': '#b78830', 'role': '鍛造師', 'role2': '效率王', 'factionName': '月餅', 'money': 2892, 'fightExp': 11, 'forgeExp': 10673, 'mineExp': 4, 'board': ['forge_exp']}, 45: {'id': 45, 'nickname': '一視同仁野格炸彈我是智障', 'color': '#a7604b', 'role': '鍛造師', 'role2': '礦 裝師', 'factionName': '烤肉', 'money': 14012, 'fightExp': 45, 'forgeExp': 10603, 'mineExp': 7, 'board': ['forge_exp']}, 73: {'id': 73, 'nickname': '梅普露', 'color': '#a7604b', 'role': '鍛造師', 'role2': '效率王', 'factionName': '烤肉', 'money': 4000, 'fightExp': 0, 'forgeExp': 9251, 'mineExp': 5, 'board': ['forge_exp']}, 517: {'id': 517, 'nickname': '西行寺幽幽子', 'color': '#a6bf70', 'role': '鍛造師', 'role2': ' 效率王', 'factionName': '文旦', 'money': 17751, 'fightExp': 9, 'forgeExp': 9081, 'mineExp': 7, 'board': ['forge_exp']}, 598: {'id': 598, 'nickname': '澄幻', 'color': '#b78830', 'role': '鍛造師', 'role2': '效率王', 'factionName': '月餅', 'money': 19362, 'fightExp': 0, 'forgeExp': 8790, 'mineExp': 3, 'board': ['forge_exp']}, 1069: {'id': 1069, 'nickname': '超 好騙多拉', 'color': '#b78830', 'role': '鍛造師', 'role2': '礦裝師', 'factionName': '月餅', 'money': 2629, 'fightExp': 3, 'forgeExp': 8743, 'mineExp': 10, 'board': ['forge_exp']}, 246: {'id': 246, 'nickname': '銀河鐵道之夜', 'color': '#a6bf70', 'role': '戰鬥員', 'role2': '礦兵', 'factionName': '文旦', 'money': 0, 'fightExp': 1740, 'forgeExp': 0, 'mineExp': 11898, 'kill': 49, 'killed': 9, 'board': ['mine_exp']}, 1177: {'id': 1177, 'nickname': '我超壯啦幹', 'color': '#b78830', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '月餅', 'money': 61, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 9103, 'board': ['mine_exp']}, 614: {'id': 614, 'nickname': 'Felicia', 'color': '#a6bf70', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '文旦', 'money': 1005, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 7002, 'board': ['mine_exp']}, 248: {'id': 248, 'nickname': '幸運礦工4號', 'color': '#a6bf70', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '文旦', 'money': 817, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 6632, 'board': ['mine_exp']}, 332: {'id': 332, 'nickname': '桐谷和人3', 'color': '#a6bf70', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '文旦', 'money': 0, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 6162, 'badge': {'color': 'red', 'borderColor': 'red.600', 'label': '茅場帥'}, 'board': ['mine_exp']}, 232: {'id': 232, 'nickname': '孟子礦工', 'color': '#a6bf70', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '文旦', 'money': 67, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 5193, 'board': ['mine_exp']}, 209: {'id': 209, 'nickname': 'STM10', 'color': '#b78830', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '月餅', 'money': 2153, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 4913, 'board': ['mine_exp']}, 873: {'id': 873, 'nickname': '惠惠醬', 'color': '#a6bf70', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '文旦', 'money': 5000, 'fightExp': 0, 'forgeExp': 31, 'mineExp': 4633, 'board': ['mine_exp']}, 727: {'id': 727, 'nickname': '放空不輕鬆', 'color': '#a6bf70', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '文旦', 'money': 1300, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 4439, 'board': ['mine_exp']}, 696: {'id': 696, 'nickname': '史蒂夫', 'color': '#a6bf70', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '文旦', 'money': 26000, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 4221, 'board': ['mine_exp']}, 235: {'id': 235, 'nickname': '孟子礦工2', 'color': '#a6bf70', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '文旦', 'money': 78, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 4136, 'board': ['mine_exp']}, 491: {'id': 491, 'nickname': 'Kc', 'color': '#a6bf70', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '文旦', 'money': 1825, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 4006, 'board': ['mine_exp']}, 776: {'id': 776, 'nickname': '好棒三點了', 'color': '#b78830', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '月餅', 'money': 59, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 4001, 'board': ['mine_exp']}, 1282: {'id': 1282, 'nickname': 'jj148s', 'color': '#a6bf70', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '文旦', 'money': 46, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 3994, 'board': ['mine_exp']}, 251: {'id': 251, 'nickname': '孟子礦工4', 'color': '#a6bf70', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '文旦', 'money': 4127, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 3993, 'board': ['mine_exp']}, 490: {'id': 490, 'nickname': '夢流希逝', 'color': '#a6bf70', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '文旦', 'money': 11986, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 3990, 'badge': {'color': 'cyan', 'borderColor': 'cyan.300', 'label': '賽狗'}, 'board': ['mine_exp']}, 273: {'id': 273, 'nickname': '孟子礦工9', 'color': '#a7604b', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '烤肉', 'money': 4187, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 3967, 'board': ['mine_exp']}, 548: {'id': 548, 'nickname': '挖哥', 'color': '#b78830', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '月餅', 'money': 0, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 3934, 'board': ['mine_exp']}, 552: {'id': 552, 'nickname': '挖挖老哥', 'color': '#b78830', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '月餅', 'money': 0, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 3905, 'board': ['mine_exp']}, 75: {'id': 75, 'nickname': '阿誠礦工2號', 'color': '#a6bf70', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '文旦', 'money': 1771, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 3902, 'board': ['mine_exp']}, 550: {'id': 550, 'nickname': '挖挖哥', 'color': '#b78830', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '月餅', 'money': 0, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 3806, 'board': ['mine_exp']}, 253: {'id': 253, 'nickname': '孟子礦工5', 'color': '#a6bf70', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '文旦', 'money': 49, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 3796, 'board': ['mine_exp']}, 411: {'id': 411, 'nickname': '霧の幻想 M1', 'color': '#a6bf70', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '文旦', 'money': 134, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 3774, 'board': ['mine_exp']}, 1030: {'id': 1030, 'nickname': '不二家1', 'color': '#b78830', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '月餅', 'money': 95, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 3731, 'board': ['mine_exp']}, 631: {'id': 631, 'nickname': '星之彩', 'color': '#a6bf70', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '文旦', 'money': 19, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 3730, 'board': ['mine_exp']}, 1006: {'id': 1006, 'nickname': '逢坂大河', 'color': '#a7604b', 'role': '礦工', 'role2': '將軍', 'factionName': '烤肉', 'money': 597, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 3730, 'board': ['mine_exp']}, 1029: {'id': 1029, 'nickname': '雙持礦工', 'color': '#b78830', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '月餅', 'money': 242, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 3673, 'board': ['mine_exp']}, 322: {'id': 322, 'nickname': '桐谷和人4', 'color': '#a6bf70', 'role': '礦工', 'role2': '雙鎬俠', 'factionName': '文旦', 'money': 1033, 'fightExp': 0, 'forgeExp': 0, 'mineExp': 3664, 'board': ['mine_exp']}, 94: {'id': 94, 'nickname': '玄日', 'color': '#a6bf70', 'role': '戰鬥員', 'role2': '衛兵', 'factionName': '文旦', 'money': 85, 'fightExp': 1102, 'forgeExp': 0, 'mineExp': 0, 'kill': 83, 'killed': 28, 'board': []}, 724: {'id': 724, 'nickname': '黑山羊幼仔', 'color': '#b78830', 'role': '戰鬥員', 'role2': '斥候', 'factionName': '月餅', 'money': 36, 'fightExp': 2505, 'forgeExp': 0, 'mineExp': 40, 'kill': 63, 'killed': 15, 'board': []}, 876: {'id': 876, 'nickname': '風涼人靜夕下', 'color': '#a6bf70', 'role': '戰鬥員', 'role2': '衛兵', 'factionName': '文旦', 'money': 371, 'fightExp': 1535, 'forgeExp': 0, 'mineExp': 143, 'kill': 63, 'killed': 12, 'board': []}, 743: {'id': 743, 'nickname': '多多鮮橙無糖微冰', 'color': '#b78830', 'role': '戰鬥員', 'role2': '衛兵', 'factionName': '月餅', 'money': 3828, 'fightExp': 2478, 'forgeExp': 0, 'mineExp': 68, 'kill': 42, 'killed': 4, 'board': []}, 121: {'id': 121, 'nickname': '梅普露 莎莉3', 'color': '#a7604b', 'role': '戰鬥員', 'role2': '破壞者', 'factionName': '烤肉', 'money': 1580, 'fightExp': 1560, 'forgeExp': 0, 'mineExp': 7, 'kill': 27, 'killed': 11, 'board': []}, 847: {'id': 847, 'nickname': '捏捏', 'color': '#a7604b', 'role': '戰鬥員', 'role2': '衛兵', 'factionName': '烤肉', 'money': 527, 'fightExp': 1760, 'forgeExp': 0, 'mineExp': 30, 'kill': 27, 'killed': 13, 'board': []}, 59: {'id': 59, 'nickname': '呱吉', 'color': '#a6bf70', 'role': '戰鬥員', 'role2': '斥候', 'factionName': '文旦', 'money': 1298, 'fightExp': 2260, 'forgeExp': 0, 'mineExp': 115, 'kill': 21, 'killed': 20, 'board': []}, 712: {'id': 712, 'nickname': '胖捏大將軍', 'color': '#a7604b', 'role': '戰鬥員', 'role2': '破壞者', 'factionName': '烤肉', 'money': 171, 'fightExp': 2587, 'forgeExp': 0, 'mineExp': 88, 'kill': 18, 'killed': 9, 'board': []}, 284: {'id': 284, 'nickname': '小豪', 'color': '#a7604b', 'role': '戰鬥員', 'role2': '衛兵', 'factionName': '烤肉', 'money': 2876, 'fightExp': 1003, 'forgeExp': 0, 'mineExp': 0, 'kill': 8, 'killed': 16, 'board': []}, 301: {'id': 301, 'nickname': 'mozzarella', 'color': '#a7604b', 'role': '戰鬥員', 'role2': '斥候', 'factionName': '烤肉', 'money': 4107, 'fightExp': 785, 'forgeExp': 0, 'mineExp': 0, 'kill': 8, 'killed': 5, 'board': []}, 483: {'id': 483, 'nickname': 'なベール2', 'color': '#a6bf70', 'role': '戰鬥員', 'role2': '衛兵', 'factionName': '文旦', 'money': 42, 'fightExp': 2351, 'forgeExp': 0, 'mineExp': 107, 'kill': 8, 'killed': 21, 'board': []}}")



    while True:
        new_leaderboard = await update_leaderboard()
        new_leaderboard_dict = {}
        for topic in new_leaderboard:
            topic_leaderboard = new_leaderboard[topic]
            for p in topic_leaderboard:
                print(p)
                if topic != 'kill':
                    p['board'] = new_leaderboard_dict.get(p['id'], {}).get('board', []) + [topic]
                else:
                    p['board'] = new_leaderboard_dict.get(p['id'], {}).get('board', [])
                new_leaderboard_dict[p['id']] = p.copy()

        text = {}
        print('dict')
        print(new_leaderboard_dict)
        print(type(new_leaderboard_dict))
        # input()
        back_prev_leaderboard = prev_leaderboard.copy()
        for p_id in new_leaderboard_dict:
            if prev_leaderboard.get(p_id) and prev_leaderboard.get(p_id)['board'] != []:
                p = new_leaderboard_dict[p_id]
                prev_p = prev_leaderboard[p_id]
                text = {}

                for stat in nl_dict:
                    if p[topic_to_stat[stat]] != prev_p[topic_to_stat[stat]]:
                        new_leaderboard_dict[p_id][stat+'_last_update'] = time.time()
                        if p[topic_to_stat[stat]] > prev_p[topic_to_stat[stat]]: 
                            text[stat] = f'【{p.get("factionName")}】{p.get("nickname")}[{p.get("role")}]({p.get("role2")}) 在{sec_to_text(p.get(stat+"_last_update", 0) - prev_p.get(stat+"_last_update", 0))}內增加了 **{p[topic_to_stat[stat]] - prev_p[topic_to_stat[stat]]}** {nl_dict[stat]} ({prev_p[topic_to_stat[stat]]} --> {p[topic_to_stat[stat]]})'
                        else:
                            assert p[topic_to_stat[stat]] < prev_p[topic_to_stat[stat]]
                            text[stat] = f'【{p.get("factionName")}】{p.get("nickname")}[{p.get("role")}]({p.get("role2")}) 在{sec_to_text(p.get(stat+"_last_update", 0) - prev_p.get(stat+"_last_update", 0))}內減少了 **{prev_p[topic_to_stat[stat]] - p[topic_to_stat[stat]]}** {nl_dict[stat]} ({prev_p[topic_to_stat[stat]]} --> {p[topic_to_stat[stat]]})'
                    
                if p.get('role2') != prev_p.get('role2'):
                    new_leaderboard_dict[p_id]['roles_last_update'] = time.time()
                    text['role2'] = f'【{p.get("factionName")}】{p.get("nickname")}[{p.get("role")}]({p.get("role2")}) 在{sec_to_text(p.get("role2_last_update", 0) - prev_p.get("role2_last_update", 0))}內更換了副職業 ({prev_p["role2"]} --> {p["role2"]})'
                
                for c in g.text_channels:
                    if c.name in channel_to_board:
                        if text.get(channel_to_board[c.name]):
                            await c.send(text[channel_to_board[c.name]])
                prev_leaderboard.pop(p_id)
            elif prev_leaderboard.get(p_id) and prev_leaderboard.get(p_id)['board'] == []:
                p = new_leaderboard_dict[p_id]
                prev_p = prev_leaderboard[p_id]
                text = {}
                for stat in nl_dict:
                    if p[topic_to_stat[stat]] != prev_p[topic_to_stat[stat]]:
                        back_prev_leaderboard[p_id][stat+'_last_update'] = time.time()
                        if p[topic_to_stat[stat]] > prev_p[topic_to_stat[stat]]: 
                            text[stat] = f'【{p.get("factionName")}】{p.get("nickname")}[{p.get("role")}]({p.get("role2")}) 在{sec_to_text(p.get(stat+"_last_update", 0) - prev_p.get(stat+"_last_update", 0))}內增加了 **{p[topic_to_stat[stat]] - prev_p[topic_to_stat[stat]]}** {nl_dict[stat]} ({prev_p[topic_to_stat[stat]]} --> {p[topic_to_stat[stat]]}) 並且回到{"、".join([nl_dict2[topic] for topic in p["board"]])}榜上'
                        else:
                            assert p[topic_to_stat[stat]] < prev_p[topic_to_stat[stat]]
                            text[stat] = f'【{p.get("factionName")}】{p.get("nickname")}[{p.get("role")}]({p.get("role2")}) 在{sec_to_text(p.get(stat+"_last_update", 0) - prev_p.get(stat+"_last_update", 0))}內減少了 **{prev_p[topic_to_stat[stat]] - p[topic_to_stat[stat]]}** {nl_dict[stat]} ({prev_p[topic_to_stat[stat]]} --> {p[topic_to_stat[stat]]}) 並且回到{"、".join([nl_dict2[topic] for topic in p["board"]])}榜上'
                    
                if p.get('role2') != prev_p.get('role2'):
                    back_prev_leaderboard[p_id]['roles_last_update'] = time.time()
                    text['role2'] = f'【{p.get("factionName")}】{p.get("nickname")}[{p.get("role")}]({p.get("role2")}) 在{sec_to_text(p.get("role2_last_update", 0) - prev_p.get("role2_last_update", 0))}內更換了副職業 ({prev_p["role2"]} --> {p["role2"]}) 並且回到{"、".join([nl_dict2[topic] for topic in p["board"]])}榜上'
                
                for c in g.text_channels:
                    if c.name in channel_to_board:
                        if text.get(channel_to_board[c.name]):
                            await c.send(text[channel_to_board[c.name]])
                
                # for stat in p['board']:
                #     if stat == 'kill':
                #         continue
                #     text[stat] = f'【{p.get("factionName")}】{p.get("nickname")}[{p.get("role")}]({p.get("role2")}) 再次登上了{"、".join([nl_dict2[topic] for topic in p["board"]])}榜 ({p[topic_to_stat[stat]]}{nl_dict[stat]})'
                prev_leaderboard.pop(p_id)
            else:
                p = new_leaderboard_dict[p_id]
                text = {}


                for stat in p['board']:
                    if stat == 'kill':
                        continue
                    # back_prev_leaderboard[prev_p_id][f'{stat}_last_update'] = time.time()
                    text[stat] = f'【{p.get("factionName")}】{p.get("nickname")}[{p.get("role")}]({p.get("role2")}) 登上了{"、".join([nl_dict2[topic] for topic in p["board"]])}榜 ({p[topic_to_stat[stat]]}{nl_dict[stat]})'

                for c in g.text_channels:
                    if c.name in channel_to_board:
                        if text.get(channel_to_board[c.name]):
                            await c.send(text[channel_to_board[c.name]])
        for prev_p_id in prev_leaderboard:
            prev_p = prev_leaderboard[prev_p_id]
            text = {}

            for stat in prev_p['board']:
                if stat == 'kill':
                    continue

                text[stat] = f'【{prev_p.get("factionName")}】{prev_p.get("nickname")}[{prev_p.get("role")}]({prev_p.get("role2")}) 從{"、".join(prev_p["board"])}榜上消失了 (原本有{p[topic_to_stat[stat]]}{nl_dict[stat]})'
            back_prev_leaderboard[prev_p_id]['board'] = []
            
            for c in g.text_channels:
                if c.name in channel_to_board:
                    if text.get(channel_to_board[c.name]):
                        await c.send(text[channel_to_board[c.name]])            

        prev_leaderboard = back_prev_leaderboard.copy()

        # for _p in new_leaderboard_dict:
        #     p = new_leaderboard_dict[_p]
        #     prev_p = prev_leaderboard.get(_p, {})
            
        #     if prev_p.get('board'):
        #         for stat in nl_dict:
        #             if p[topic_to_stat[stat]] != prev_p[topic_to_stat[stat]]:
        #                 p[stat+'_last_update'] = time.time()
        #                 if p[topic_to_stat[stat]] > prev_p[topic_to_stat[stat]]: 
        #                     text[stat] = f'【{p.get("factionName")}】{p.get("nickname")}[{p.get("role")}]({p.get("role2")}) 在{sec_to_text(p.get(stat+"_last_update", 0) - prev_p.get(stat+"_last_update", 0))}內增加了 **{p[topic_to_stat[stat]] - prev_p[topic_to_stat[stat]]}** {nl_dict[stat]} ({prev_p[topic_to_stat[stat]]} --> {p[topic_to_stat[stat]]})'
        #                 else:
        #                     assert p[topic_to_stat[stat]] < prev_p[topic_to_stat[stat]]
        #                     text[stat] = f'【{p.get("factionName")}】{p.get("nickname")}[{p.get("role")}]({p.get("role2")}) 在{sec_to_text(p.get(stat+"_last_update", 0) - prev_p.get(stat+"_last_update", 0))}內減少了 **{prev_p[topic_to_stat[stat]] - p[topic_to_stat[stat]]}** {nl_dict[stat]} ({prev_p[topic_to_stat[stat]]} --> {p[topic_to_stat[stat]]})'
                    
        #         if p.get('role2') != prev_p.get('role2'):
        #             p['roles_last_update'] = time.time()
        #             text['role2'] = f'【{p.get("factionName")}】{p.get("nickname")}[{p.get("role")}]({p.get("role2")}) 在{sec_to_text(p.get("role2_last_update", 0) - prev_p.get("role2_last_update", 0))}內更換了副職業 ({prev_p["role2"]} --> {p["role2"]})'
        #         prev_leaderboard.pop(p['id'])
        #     else:
        #         prev_leaderboard[p['id']] = new_leaderboard_dict[p['id']]
        #         for stat in p['board']:
        #             if stat == 'kill':
        #                 continue
                    
        #             text[stat] = f'【{p.get("factionName")}】{p.get("nickname")}[{p.get("role")}]({p.get("role2")}) 登上了{"、".join([nl_dict2[topic] for topic in p["board"]])}榜 ({p[topic_to_stat[stat]]}{nl_dict[stat]})'

        #     new_leaderboard_dict[p['id']] = p.copy()
        #     for c in g.text_channels:
        #         if c.name in channel_to_board:
        #             if text.get(channel_to_board[c.name]):
        #                 await c.send(text[channel_to_board[c.name]])
        # for _p in prev_leaderboard:
        #     prev_p = prev_leaderboard[_p]
        #     for stat in prev_p['board']:
        #         if stat == 'kill':
        #             continue
        #         text[stat] = f'【{prev_p.get("factionName")}】{prev_p.get("nickname")}[{prev_p.get("role")}]({prev_p.get("role2")}) 從{"、".join(prev_p["board"])}榜上消失了 (原本有{p[topic_to_stat[stat]]}{nl_dict[stat]})'
        #     prev_p['board'] = []
        #     new_leaderboard_dict[prev_p['id']] = prev_p.copy()
        #     for c in g.text_channels:
        #         if c.name in channel_to_board:
        #             if text.get(channel_to_board[c.name]):
        #                 await c.send(text[channel_to_board[c.name]])

        # for p in new_leaderboard_dict:
        #     prev_leaderboard[p['id']] = new_leaderboard_dict[p['id']]

        # print(prev_leaderboard)



        await asyncio.sleep(10)

client.run(os.getenv('siesta-token'))
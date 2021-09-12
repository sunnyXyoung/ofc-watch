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

    return now_leaderboard_dict

client = discord.Client()

# log = open(os.path.join(webroot, 'ofc', f'{round}.leaderboard'), 'a', encoding="utf-8")


@client.event
async def on_ready():
    print(f'{client.user} online')
    for g in client.guilds:
        if g.id == 678210712824315924:
            break


    prev_leaderboard = {}

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

        print(new_leaderboard_dict)
        print(type(new_leaderboard_dict))
        input()
        for _p in new_leaderboard_dict:
            p = new_leaderboard_dict[_p]
            prev_p = prev_leaderboard.get(p['id'], {})
            
            if prev_p.get('board'):
                for stat in nl_dict:
                    if p[topic_to_stat[stat]] != prev_p[topic_to_stat[stat]]:
                        p[stat+'_last_update'] = time.time()
                        if p[topic_to_stat[stat]] > prev_p[topic_to_stat[stat]]: 
                            text[stat] = f'【{p.get("factionName")}】{p.get("nickname")}[{p.get("role")}]({p.get("role2")}) 在{sec_to_text(p.get(stat+"_last_update", 0) - prev_p.get(stat+"_last_update", 0))}內增加了 **{p[topic_to_stat[stat]] - prev_p[topic_to_stat[stat]]}** {nl_dict[stat]} ({prev_p[topic_to_stat[stat]]} --> {p[topic_to_stat[stat]]})'
                        else:
                            assert p[topic_to_stat[stat]] < prev_p[topic_to_stat[stat]]
                            text[stat] = f'【{p.get("factionName")}】{p.get("nickname")}[{p.get("role")}]({p.get("role2")}) 在{sec_to_text(p.get(stat+"_last_update", 0) - prev_p.get(stat+"_last_update", 0))}內減少了 **{prev_p[topic_to_stat[stat]] - p[topic_to_stat[stat]]}** {nl_dict[stat]} ({prev_p[topic_to_stat[stat]]} --> {p[topic_to_stat[stat]]})'
                    
                if p.get('role2') != prev_p.get('role2'):
                    p['roles_last_update'] = time.time()
                    text['role2'] = f'【{p.get("factionName")}】{p.get("nickname")}[{p.get("role")}]({p.get("role2")}) 在{sec_to_text(p.get("role2_last_update", 0) - prev_p.get("role2_last_update", 0))}內更換了副職業 ({prev_p["role2"]} --> {p["role2"]})'
                prev_leaderboard.pop(p['id'])
            else:
                prev_leaderboard[p['id']] = new_leaderboard_dict[p['id']]
                for stat in p['board']:
                    if stat == 'kill':
                        continue
                    
                    text[stat] = f'【{p.get("factionName")}】{p.get("nickname")}[{p.get("role")}]({p.get("role2")}) 登上了{"、".join([nl_dict2[topic] for topic in p["board"]])}榜 ({p[topic_to_stat[stat]]}{nl_dict[stat]})'

            new_leaderboard_dict[p['id']] = p.copy()
            for c in g.text_channels:
                if c.name in channel_to_board:
                    if text.get(channel_to_board[c.name]):
                        await c.send(text[channel_to_board[c.name]])
        for _p in prev_leaderboard:
            prev_p = prev_leaderboard[_p]
            for stat in prev_p['board']:
                if stat == 'kill':
                    continue
                text[stat] = f'【{prev_p.get("factionName")}】{prev_p.get("nickname")}[{prev_p.get("role")}]({prev_p.get("role2")}) 從{"、".join(prev_p["board"])}榜上消失了 (原本有{p[topic_to_stat[stat]]}{nl_dict[stat]})'
            prev_p['board'] = []
            new_leaderboard_dict[prev_p['id']] = prev_p.copy()
            for c in g.text_channels:
                if c.name in channel_to_board:
                    if text.get(channel_to_board[c.name]):
                        await c.send(text[channel_to_board[c.name]])

        for p in new_leaderboard_dict:
            prev_leaderboard[p['id']] = new_leaderboard_dict[p['id']]

        print(prev_leaderboard)



        await asyncio.sleep(600)

client.run(os.getenv('siesta-token'))
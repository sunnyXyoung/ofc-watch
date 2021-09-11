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
}
logging.basicConfig(level=logging.NOTSET)

async def update_leaderboard():
    
    leaderboards = ['money', 'fight_exp', 'forge_exp', 'mine_exp']
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
                logging.error(faction_dict, faction_dict.text, faction_dict.status_code)
                error_count += 1
                if error_count > 10:
                    logging.error('over 10 errors')
                    exit()
            else:
                break
        now_leaderboard_dict[i] = json.loads(response.text)

    return now_leaderboard_dict

client = discord.Client()

# log = open(os.path.join(webroot, 'ofc', f'{round}.leaderboard'), 'a', encoding="utf-8")


@client.event
async def on_ready():
    print(f'{client.user} online')
    for g in client.guilds:
        if g.id == 881543633290035211:
            break


    leaderboard = {}
    while True:
        new_leaderboard = await update_leaderboard()

        
        for c in g.text_channels:
            if c.name == faction:
                await c.send(text)

        await asyncio.sleep(10)

client.run(os.getenv('siesta-token'))
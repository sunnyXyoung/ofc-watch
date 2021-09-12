from discord_components import *
import discord_components
import discord
import json
import time
import random
import datetime
import asyncio
from dotenv import load_dotenv
import sys
load_dotenv()


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    DiscordComponents(client)
    print(f'{client.user} online')


@client.event
async def on_message(message):
    if message.content.strip() == 'k!search':
        await message.reply('''```
k!search [-r round] [-p player_name,player_name2] [-l location] [-w weapon_type,weapon_type2,...] ["search_text"]
-r 指定輪數
-p 指定玩家名稱，若玩家名稱包含在內就會顯示
-l 指定位置
-w 指定武器類別
"search_text" 指定所有包含該段文字的戰報

除-r為必填以外，其餘欄位最少要指定一個。
```''')


    elif message.startswith('k!search '):        
        search_text = message.content.strip()[len('k!search '):].lower()
        search_text = search_text.split(' ')
        search_params = []
        for i in search_text:
            if i:
                search_params.append(i)

        if '-r' in search_params and search_params.index('-r') != len(search_params)-1:
            

        else:
            await message.reply('未指定輪數 請使用 `k!search` 查看更多資訊')
        

client.run(os.getenv('siesta-token'))
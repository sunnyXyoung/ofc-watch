from discord import Client
from discord_components import *
import discord_components
import discord
import json
import time
import random
import datetime
import asyncio



intents = discord.Intents.default()
intents.members = True

client = Client(intents=intents)


@client.event
async def on_ready():
    DiscordComponents(client)
    print(f'{client.user} online')


@client.event
async def on_message(message):
    
    
    if message.content.strip() == 'k!search':
        await message.reply('''```
k!search [-p player_name,player_name2] [-l location] [-w weapon_type,weapon_type2,...] ["search_text"]
-p 指定玩家名稱，若玩家名稱包含在內就會顯示
-l 指定位置
-w 指定武器類別
"search_text" 指定所有包含該段文字的戰報
```''')


    elif message.startswith('k!search '):        
        seach_text = message.content.strip()[len('k!search '):].lower()
        

client.run("Njk3NjYyMDA4Mzc1Mzc3OTY1.Xo6iYA.noG-FcNH3QTxcKFduexwoUWfO6w")
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
import os
load_dotenv()


client = discord.Client()

webroot = os.getenv('web-root')

param_to_text = {
    '-R': '輪數：',
    '-p': '玩家名稱：',
    '-r': '職業：',
    '-r2': '副職業：',
    '-l': '位置：',
    '-w': '武器類別：',
    '-wn': '武器名稱：',
    '-s': '查詢文字：',
}

@client.event
async def on_ready():
    DiscordComponents(client)
    print(f'{client.user} online')


@client.event
async def on_message(message):
    if message.content.strip() == 'k!search':
        await message.reply('''
`k!search [-R round] [-p player_name,player_name2] [-r role,role] [-r2 role2,role2] [-l location] [-w weapon_type,weapon_type2,...] [-wn weapon_name,weapon_name2] [-s "search_text"]`
-R 指定輪數
-p 指定玩家名稱，若玩家名稱包含在內就會顯示
-r 指定職業
-r2 指定副職業
-l 指定位置
-w 指定武器類別
-wn 指定武器名稱
-s 指定所有包含該段文字的戰報

除-r為必填以外，其餘欄位最少要指定一個。
範例：`k!search "第 74 層被摧毀了"`
範例：`k!search -p Kulimi 層被摧毀了`
範例：`k!search -p "Kulimi Beta" 層被摧毀了`
範例：`k!search -r 礦工,戰鬥員`
''')
    elif message.content.startswith('k!search '):
        if 885399145005846538 not in [r.id for r in message.author.roles]:
            await message.reply('此為高階功能 請使用 `k!battle` 查看更多關於高階會員的資訊')
            return

        search_text = message.content.strip()[len('k!search '):] + ' '

        # search_text = search_text.split(' ')
        search_params = []
        temp_param = ''
        start_quote = False
        for i in search_text:
            if i == ' ' and not start_quote:
                if temp_param != '':
                    search_params.append(temp_param)
                    temp_param = ''
            elif i == '"':
                if start_quote:
                    start_quote = False
                else:
                    start_quote = True
            else:
                temp_param = temp_param + i

        # print(search_params)

        if '-R' in search_params and search_params.index('-R') != len(search_params)-1:
            _round = search_params[search_params.index('-R')+1]
            if _round in os.listdir(os.path.join(webroot, 'ofc')):
                del search_params[search_params.index('-R')+1]
                del search_params[search_params.index('-R')]
                
                if len(search_params) % 2 == 0:
                    params = {}
                    for i in range(len(search_params) // 2):
                        params[search_params[2*i]] = search_params[2*i+1]
                    for i in params:
                        if i not in param_to_text:
                            await message.reply(f'未知的參數 `{i}` 請使用 `k!search` 查看更多資訊')
                            return
                    
                    search_embed = discord.Embed(
                        title = "請確認參數是否正確", 
                        colour = discord.Colour.random(seed=time.time()),
                        description = 'k!search 戰報查詢系統',
                        timestamp = datetime.datetime.utcfromtimestamp(time.time()),
                    )
                    search_embed.insert_field_at(index=0, name='參數設定', value=('```js\n' + '\n'.join([f"{param_to_text[i]}{params[i]}" for i in params]) + '\n```'), inline=False)
                    search_embed.set_footer(text=f"第 {_round} 輪")
                    search_m = await message.reply(embed=search_embed)


                else:
                    await message.reply('格式不正確 請使用 `k!search` 查看更多資訊')
            else:
                await message.reply('無該輪數資料 請使用 `k!search` 查看更多資訊')
        else:
            await message.reply('未指定輪數 請使用 `k!search` 查看更多資訊')
        

client.run(os.getenv('siesta-token'))
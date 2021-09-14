from discord_components import *
import discord_components
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
import search_filter
load_dotenv()


client = discord.Client()
webroot = os.getenv('web-root')

@client.event
async def on_ready():
    DiscordComponents(client)
    print(f'login as {client.user}')


@client.event
async def on_message(message):
    if message.content.startswith('k!show '):
        a = message.content[len('k!show '):].split(' ')
        if len(a) == 1:
            _round = '9'
            report_f_l = a[0] + '.json'
        else:
            _round = a[0]
            report_f_l = a[1] + '.json'
        if _round in os.listdir(os.path.join(webroot, 'ofc')):
            if report_f_l in os.listdir(os.path.join(webroot, 'ofc', _round)):
                with open(os.path.join(webroot, 'ofc', _round, report_f_l), 'r', encoding='utf8') as json_file:
                    report = json.loads(json_file.read())
                    r_embed = search_filter.report_to_embed(report, _round, f"第 {_round} 輪 k!show")
                    await message.reply(embed=r_embed, components=[[Button(style=ButtonStyle.gray, label="上一份戰報"),Button(style=ButtonStyle.gray, label="下一份戰報"),]])
            else:
                await message.reply('該輪數無此戰報')    
        else:
            await message.reply('無該輪數資料')
    elif message.content == 'k!show':
        await message.reply('`k!show [<round>] <id>`\n範例：`k!show 9 9999`\n若無指定輪數則會使用最新的一輪')

@client.event
async def on_button_click(res):
    print(res.message.embeds[0].footer)
    if 'k!show' in res.message.embeds[0].footer.text:
        params = res.message.embeds[0].author.url.split('/')
        print(params)
        _round = params[-2]
        r_id = int(params[-1])
        r_len = len(os.listdir(os.path.join(webroot, 'ofc', _round)))
        if res.component.label == '上一份戰報':
            r_id = (r_id - 2) % r_len + 1
        elif res.component.label == '下一份戰報':
            r_id = r_id % r_len + 1
        with open(os.path.join(webroot, 'ofc', _round, f'{r_id}.json'), 'r', encoding='utf8') as json_file:
            report = json.loads(json_file.read())
            r_embed = search_filter.report_to_embed(report, _round, f"第 {_round} 輪 k!show")
            await res.message.edit(embed=r_embed, components=[[Button(style=ButtonStyle.gray, label="上一份戰報"),Button(style=ButtonStyle.gray, label="下一份戰報"),]])
            await res.respond(type=6)
        
client.run(os.getenv('autokulimi-token'))

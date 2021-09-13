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
import search_filter
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
    '-Wp': '贏家玩家名稱：',
    '-Wr': '贏家職業：',
    '-Wr2': '贏家副職業：',
    '-Ww': '贏家武器類別：',
    '-Wwn': '贏家武器名稱：',
    '-Lp': '輸家玩家名稱：',
    '-Lr': '輸家職業：',
    '-Lr2': '輸家副職業：',
    '-Lw': '輸家武器類別：',
    '-Lwn': '輸家武器名稱：',
}

@client.event
async def on_ready():
    DiscordComponents(client)
    print(f'{client.user} online')


@client.event
async def on_message(message):
    if message.content.strip() == 'k!search':
        await message.reply('''
`k!search <params>`
-R 指定輪數
-p 指定玩家名稱，若玩家名稱包含在內就會顯示
-r 指定職業
-r2 指定副職業
-l 指定位置
-w 指定武器類別
-wn 指定武器名稱
-f 指定陣營，須完全正確
-s 指定所有包含該段文字的戰報

-Wp 指定贏家玩家名稱，若玩家名稱包含在內就會顯示
-Wr 指定贏家職業
-Wr2 指定贏家副職業
-Ww 指定贏家武器類別
-Wf 指定贏家陣營，須完全正確
-Wwn 指定贏家武器名稱

-Lp 指定輸家玩家名稱，若玩家名稱包含在內就會顯示
-Lr 指定輸家職業
-Lr2 指定輸家副職業
-Lw 指定輸家武器類別
-Lf 指定輸家陣營，須完全正確
-Lwn 指定輸家武器名稱

除-R為必填以外，其餘欄位最少要指定一個。
範例：`k!search -R 9 -s "第 74 層被摧毀了"`
範例：`k!search -R 6 -p Kulimi -s 層被摧毀了`
範例：`k!search -R 5 -p "Kulimi Beta" -s 層被摧毀了`
範例：`k!search -R 5.5 -r 礦工,戰鬥員`
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
            if (i == ' ' or i == '\n') and not start_quote:
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
                        colour = discord.Colour.blue(),
                        description = 'k!search 戰報查詢系統',
                        timestamp = datetime.datetime.utcfromtimestamp(time.time()),
                    )
                    search_embed.insert_field_at(index=0, name='參數設定', value=('```js\n' + '\n'.join([f"{param_to_text[i]}{params[i]}" for i in params]) + '\n```'), inline=False)
                    search_embed.set_footer(text=f"第 {_round} 輪")
                    search_m = await message.reply(embed=search_embed,
                        components=[[                        
                            Button(style=ButtonStyle.red, label="確認"),
                            Button(style=ButtonStyle.gray, label="取消"),
                        ]],
                    )
                    wait_time = time.time()
                    refuse = False
                    while True:
                        try:
                            res = await client.wait_for("button_click", timeout=60.0)
                            if res.message.id == search_m.id:
                                await res.respond(type=6)
                                break
                        except Exception as e:
                            print(e)
                            if time.time() - wait_time > 60:
                                refuse = True
                                search_embed = discord.Embed(
                                    title = "閒置過久，已取消搜尋", 
                                    colour = discord.Colour.red(),
                                    description = 'k!search 戰報查詢系統',
                                    timestamp = datetime.datetime.utcfromtimestamp(time.time()),
                                )
                                search_embed.set_author(name=str(message.author), icon_url=message.author.avatar_url)
                                search_embed.insert_field_at(index=0, name='參數設定', value=('```js\n' + '\n'.join([f"{param_to_text[i]}{params[i]}" for i in params]) + '\n```'), inline=False)
                                search_embed.set_footer(text=f"第 {_round} 輪")
                                await search_m.edit(embed=search_embed, components=[])
                                return

                    if not refuse and res.component.label == '確認':
                        search_embed = discord.Embed(
                            title = "開始搜尋", 
                            colour = discord.Colour.green(),
                            description = 'k!search 戰報查詢系統',
                            timestamp = datetime.datetime.utcfromtimestamp(time.time()),
                        )
                        search_embed.set_author(name=str(res.user), icon_url=res.user.avatar_url)
                        search_embed.insert_field_at(index=0, name='參數設定', value=('```js\n' + '\n'.join([f"{param_to_text[i]}{params[i]}" for i in params]) + '\n```'), inline=False)
                        search_embed.set_footer(text=f"第 {_round} 輪")
                        await search_m.edit(embed=search_embed, components=[])
                        
                        ans_list = []
                        for report_f in os.listdir(os.path.join(webroot, 'ofc', _round)):
                            with open(os.path.join(webroot, 'ofc', _round, report_f), 'r', encoding='utf8') as json_file:
                                report = json.loads(json_file.read())
                                # report = report['report']
                                pass_check = True
                                for test in params:
                                    if not getattr(search_filter, test.replace('-', ''))(report, params[test]):
                                        pass_check = False
                                        break

                                if pass_check:
                                    ans_list.append(report_f.replace('.json', ''))
                        if len(ans_list) == 0:
                            ans_embed = discord.Embed(
                                title = "無符合的結果", 
                                colour = discord.Colour.dark_magenta(),
                                description = 'k!search 戰報查詢系統',
                                timestamp = datetime.datetime.utcfromtimestamp(time.time()),
                            )
                            ans_embed.set_author(name=str(message.author), icon_url=message.author.avatar_url)
                            await search_m.reply(embed=ans_embed, components=[])
                        else:
                            ans_embed = discord.Embed(title="生成結果中，請稍後")
                            ans_m = await search_m.reply(embed=ans_embed)
                            while True:
                                ans_embed = discord.Embed(
                                    title = f"搜尋結果：共筆 {len(ans_list)} 戰報符合條件",
                                    colour = discord.Colour.dark_blue(),
                                    description = 'k!search 戰報查詢系統',
                                    timestamp = datetime.datetime.utcfromtimestamp(time.time()),
                                )
                                ans_embed.set_author(name=str(message.author), icon_url=message.author.avatar_url)
                                ans_embed.set_footer(text=f"第 {_round} 輪")
                                await ans_m.edit(embed=ans_embed, components=
                                        [[
                                            Button(style=ButtonStyle.gray, label="預覽戰報"),
                                            Button(style=ButtonStyle.gray, label="查看列表"),
                                            Button(style=ButtonStyle.red, label="退出")
                                        ]]
                                    )
                                while True:
                                    try:
                                        res = await client.wait_for("button_click", timeout=60.0)
                                        if res.message.id == ans_m.id:
                                            await res.respond(type=6)
                                            break
                                    except Exception as e:
                                        print(e)
                                        if time.time() - wait_time > 60:
                                            refuse = True
                                            ans_embed = discord.Embed(
                                                title = f"搜尋結果：共筆 {len(ans_list)} 戰報符合條件",
                                                colour = discord.Colour.red(),
                                                description = 'k!search 戰報查詢系統',
                                                timestamp = datetime.datetime.utcfromtimestamp(time.time()),
                                            )
                                            ans_embed.set_footer(text=f"第 {_round} 輪")
                                            ans_embed.set_author(name=str(message.author), icon_url=message.author.avatar_url)
                                            ans_embed.insert_field_at(index=0, name="閒置過久，已退出檢視", value='閒置60秒後將會自動退出')
                                            await ans_m.edit(embed=ans_embed, components=[])
                                            return
    
                                if res.component.label == "退出":
                                    ans_embed = discord.Embed(
                                        title = f"搜尋結果：共筆 {len(ans_list)} 戰報符合條件",
                                        colour = discord.Colour.red(),
                                        description = 'k!search 戰報查詢系統',
                                        timestamp = datetime.datetime.utcfromtimestamp(time.time()),
                                    )
                                    ans_embed.set_footer(text=f"第 {_round} 輪")
                                    ans_embed.set_author(name=str(message.author), icon_url=message.author.avatar_url)
                                    ans_embed.insert_field_at(index=0, name="已退出檢視", value='感謝你的使用')
                                    await ans_m.edit(embed=ans_embed, components=[])
                                    return
                                elif res.component.label == "查看列表":
                                    text = '\n'.join([f"https://ofc-watch.kulimi.tw/history/{_round}/{i}" for i in ans_list])
                                    if len(text) > 1024:
                                        ans_embed = discord.Embed(
                                            title = f"搜尋結果：共 {len(ans_list)} 筆戰報符合條件",
                                            colour = discord.Colour.red(),
                                            description = 'k!search 戰報查詢系統',
                                            timestamp = datetime.datetime.utcfromtimestamp(time.time()),
                                        )
                                        ans_embed.set_footer(text=f"第 {_round} 輪")
                                        ans_embed.set_author(name=str(message.author), icon_url=message.author.avatar_url)
                                        ans_embed.remove_field(0)
                                        ans_embed.insert_field_at(index=0, name="戰報過多，無法查看列表", value='總和超過1024個字')
                                        await ans_m.edit(embed=ans_embed)
                                    else:
                                        ans_embed.remove_field(0)
                                        ans_embed.insert_field_at(index=0, name=f'結果列表', value=text, inline=False)
                                        await ans_m.edit(embed=ans_embed, components=[Button(style=ButtonStyle.red, label="返回")])
                                        while True:
                                            try:
                                                res = await client.wait_for("button_click", timeout=60.0)
                                                if res.message.id == ans_m.id:
                                                    await res.respond(type=6)
                                                    break
                                            except Exception as e:
                                                print(e)
                                                if time.time() - wait_time > 60:
                                                    refuse = True
                                                    ans_embed = discord.Embed(
                                                        title = f"搜尋結果：共筆 {len(ans_list)} 戰報符合條件",
                                                        colour = discord.Colour.red(),
                                                        description = 'k!search 戰報查詢系統',
                                                        timestamp = datetime.datetime.utcfromtimestamp(time.time()),
                                                    )
                                                    ans_embed.set_footer(text=f"第 {_round} 輪")
                                                    ans_embed.set_author(name=str(message.author), icon_url=message.author.avatar_url)
                                                    ans_embed.insert_field_at(index=0, name="閒置過久，已退出檢視", value='閒置60秒後將會自動退出')
                                                    await ans_m.edit(embed=ans_embed, components=[])
                                                    return


                                elif res.component.label == "預覽戰報":
                                    index = 0
                                    ans_len = len(ans_list)
                                    while True:
                                        with open(os.path.join(webroot, 'ofc', _round, ans_list[index]+'.json'), 'r', encoding='utf8') as json_file:
                                            print('open', ans_list[index])
                                            report = json.loads(json_file.read())
                                            ans_embed = search_filter.report_to_embed(report, _round, f"搜尋結果：共 {len(ans_list)} 筆戰報符合條件")
                                            await ans_m.edit(embed=ans_embed, components=[
                                                    [
                                                        Button(style=ButtonStyle.gray, label="上一份戰報"),
                                                        Button(style=ButtonStyle.gray, label="下一份戰報"),
                                                        Button(style=ButtonStyle.blue, label="回到結果"),
                                                        Button(style=ButtonStyle.red, label="退出")
                                                    ]
                                                ])
                                        while True:
                                            print('wait btn click')
                                            try:
                                                res = await client.wait_for("button_click", timeout=60.0)
                                                if res.message.id == ans_m.id:
                                                    await res.respond(type=6)
                                                    break
                                            except Exception as e:
                                                print(e)
                                                if time.time() - wait_time > 60:
                                                    refuse = True
                                                    ans_embed = discord.Embed(
                                                        title = f"搜尋結果：共筆 {len(ans_list)} 戰報符合條件",
                                                        colour = discord.Colour.red(),
                                                        description = 'k!search 戰報查詢系統',
                                                        timestamp = datetime.datetime.utcfromtimestamp(time.time()),
                                                    )
                                                    ans_embed.set_footer(text=f"第 {_round} 輪")
                                                    ans_embed.set_author(name=str(message.author), icon_url=message.author.avatar_url)
                                                    ans_embed.insert_field_at(index=0, name="閒置過久，已退出檢視", value='閒置60秒後將會自動退出')
                                                    await ans_m.edit(embed=ans_embed, components=[])
                                                    return
                                        if res.component.label == '上一份戰報':
                                            index = (index - 1) % ans_len
                                        elif res.component.label == '下一份戰報':
                                            index = (index + 1) % ans_len
                                        elif res.component.label == '回到結果':
                                            break
                                        elif res.component.label == '退出':
                                            ans_embed = discord.Embed(
                                                title = f"搜尋結果：共筆 {len(ans_list)} 戰報符合條件",
                                                colour = discord.Colour.red(),
                                                description = 'k!search 戰報查詢系統',
                                                timestamp = datetime.datetime.utcfromtimestamp(time.time()),
                                            )
                                            ans_embed.set_footer(text=f"第 {_round} 輪")
                                            ans_embed.set_author(name=str(message.author), icon_url=message.author.avatar_url)
                                            ans_embed.insert_field_at(index=0, name="已退出檢視", value='感謝你的使用')
                                            await ans_m.edit(embed=ans_embed, components=[])
                                            return




                    else:
                        search_embed = discord.Embed(
                            title = "已取消搜尋", 
                            colour = discord.Colour.red(),
                            description = 'k!search 戰報查詢系統',
                            timestamp = datetime.datetime.utcfromtimestamp(time.time()),
                        )
                        search_embed.set_author(name=str(res.user), icon_url=res.user.avatar_url)
                        search_embed.insert_field_at(index=0, name='參數設定', value=('```js\n' + '\n'.join([f"{param_to_text[i]}{params[i]}" for i in params]) + '\n```'), inline=False)
                        search_embed.set_footer(text=f"第 {_round} 輪")
                        await search_m.edit(embed=search_embed, components=[])
                        return

                else:
                    await message.reply('格式不正確 請使用 `k!search` 查看更多資訊')
            else:
                await message.reply('無該輪數資料 請使用 `k!search` 查看更多資訊')
        else:
            await message.reply('未指定輪數 請使用 `k!search` 查看更多資訊')
        

client.run(os.getenv('siesta-token'))
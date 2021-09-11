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

client = discord.Client()


def get_report(report_id):
    headers = {
        'User-Agent': 'I just wanna know all the secret data',
        'Accept': '*/*',
        'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'token': os.getenv('watch-token'),
        'Origin': 'https://ourfloatingcastle.com',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }
    get_response = requests.get(f'https://api.ourfloatingcastle.com/api/report/{report_id}', headers=headers)
    return get_response


def get_faction():
    headers = {
        'User-Agent': 'I just wanna know all the secret data',
        'Accept': '*/*',
        'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        
        'Origin': 'https://ourfloatingcastle.com',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }
    get_response = requests.get('https://api.ourfloatingcastle.com/api/factions/overview', headers=headers)
    return get_response


@client.event
async def on_ready():
    print(f'{client.user} online')
    for g in client.guilds:
        if g.id == 881543633290035211:
            for c in g.text_channels:
                if c.id == 886207121685901322:
                    lastest_report_c = c
                    break
            else:
                continue
            break

    faction_dict = get_faction()
    if faction_dict.status_code != 200:
        logging.error(faction_dict, faction_dict.text, faction_dict.status_code)
        exit()
    faction_dict = json.loads(faction_dict.text)

    faction_list= faction_dict['factions']
    faction_dict = {}
    for faction in faction_list:
        faction_dict[faction['name']] = faction

    logging.basicConfig(level=logging.NOTSET)
    try: _round = sys.argv[1]
    except IndexError: _round = '6'
    webroot = os.getenv('web-root')
    initial_wait_time = 10
    wait_time = initial_wait_time
    wait_time_rate = 1.5
    max_wait_time = 600

    try: os.mkdir(os.path.join(webroot, 'ofc', _round))
    except FileExistsError: pass
    exist_report = {}
    for i in os.listdir(os.path.join(webroot, 'ofc', _round)):
        if '.json' in i: exist_report[int(i[:-5])] = i

    try:
        for i in range(1, sorted(exist_report.items())[-1][0]+1):
            if f'{i}.json' != exist_report.get(i, ''):
                with open(os.path.join(webroot, 'ofc', _round, f'{i}.json'), 'w', encoding="utf-8") as f:
                    f.write(json.dumps(json.loads(get_report(i).text), ensure_ascii=False))
        i = sorted(exist_report.items())[-1][0]
    except IndexError:
        i = 1

    while True:
        logging.info(i)
        initial_time = time.time()  # Record initial time.
        response = get_report(i)
        logging.info(response.text)

        if response.status_code == 200:
            try:
                line_dict = json.loads(response.text)
                with open(os.path.join(webroot, 'ofc', _round, f'{i}.json'), 'w', encoding="utf-8") as f:
                    f.write(json.dumps(line_dict, ensure_ascii=False))

                # text = f"https://ofc-watch.kulimi.tw/history/{_round}/{i}"
                line_dict = line_dict['report']
                while True:
                    for faction in faction_dict:
                        if line_dict['location'].startswith(faction):
                            break
                        else:
                            logging.error('unknown faction')
                    else:
                        _faction_dict = get_faction()
                        if _faction_dict.status_code != 200:
                            logging.error(_faction_dict, _faction_dict.text, _faction_dict.status_code)
                            exit()
                        _faction_dict = json.loads(faction_dict.text)
                        _faction_list = _faction_dict['factions']
                        faction_dict = {}
                        for faction in _faction_list:
                            faction_dict[faction['name']] = faction
                        continue
                    break
                
                summary = '戰報'

                for m in line_dict['messages']['messages']:
                    a = m['m'].split(' ')
                    if m.get('s') == 'critical' and ([a[0], a[2]] == [f"{line_dict['aName']}被擊殺身亡了，{line_dict.get('bName', '')}還有", "點體力"] or [a[0], a[2]] == [f"{line_dict.get('bName', '')}被擊殺身亡了，{line_dict['aName']}還有", "點體力"]) and faction == line_dict['aFactionName']:
                        summary = '[衛兵] ' + m['m']
                    elif m.get('s') == 'critical' and ([a[0], a[2]] == [f"{line_dict['aName']}被擊殺身亡了，{line_dict.get('bName', '')}還有", "點體力"] or [a[0], a[2]] == [f"{line_dict.get('bName', '')}被擊殺身亡了，{line_dict['aName']}還有", "點體力"]):
                        summary = m['m']
                        break
                    elif m.get('s') == 'critical' and a[:-1] == f"獲得了{line_dict['location'][len(faction):]}獎勵".split(' '):
                        summary = m['m']
                        break
                    elif m.get('s') == 'critical' and m['m'] == f"{line_dict['location'][len(faction):]}被摧毀了":
                        summary = m['m']
                        break
                    elif a[0] == f'{line_dict["aName"]}直接攻擊城堡，造成' and a[2] == '點傷害':
                        summary = m['m']
                        break
                    elif m.get('s') == 'info' and m['m'].startswith('雙方大戰 16 回合不分勝負！'):
                        summary = m['m']
                        break


                t = discord.Embed(title=summary, description=f"在 **{line_dict['location']}**", colour=(int(faction_dict[faction]['color'].replace('#', ''), 16)), timestamp=datetime.datetime.utcfromtimestamp(line_dict['time'] / 1000))
                t.set_author(name=f"戰報編號{i}", url=f"https://ofc-watch.kulimi.tw/history/{_round}/{i}")

                equip_list = '\n'.join([f"{weapon['quality']}的 **{weapon['name']}**（{weapon['type']}）攻擊{weapon['atk']}、防禦{weapon['def']}、礦力{weapon['minePower']}" for weapon in line_dict['messages']['stats']['a']['equipments']])
                text = f"陣營：**{line_dict['aFactionName']}**\n玩家：**{line_dict['aName']}**\n職業：**{line_dict['messages']['stats']['a']['role']}**\n副職：**{line_dict['messages']['stats']['a']['role2']}**\nHP：**{line_dict['messages']['stats']['a']['hp']}**\n熟練：**{line_dict['messages']['stats']['a']['fightExp']}**\nID：**{line_dict['aId']}**\n裝備：\n{equip_list}"
                t.add_field(name="**攻擊方**", value=text, inline=True)
                
                if line_dict.get('bName'):
                    equip_list = '\n'.join([f"{weapon['quality']}的 **{weapon['name']}**（{weapon['type']}）攻擊{weapon['atk']}、防禦{weapon['def']}、礦力{weapon['minePower']}" for weapon in line_dict['messages']['stats']['b']['equipments']])
                    text = f"陣營：**{line_dict['bFactionName']}**\n玩家：**{line_dict['bName']}**\n職業：**{line_dict['messages']['stats']['b']['role']}**\n副職：**{line_dict['messages']['stats']['b']['role2']}**\nHP：**{line_dict['messages']['stats']['b']['hp']}**\n熟練：**{line_dict['messages']['stats']['b']['fightExp']}**\nID：**{line_dict['bId']}**\n裝備：\n{equip_list}"
                else:
                    text = faction_dict['location'] + '的城牆'
                t.add_field(name="**防守方**", value=text, inline=True)
                await lastest_report_c.send(embed=t)


                i += 1
                wait_time = initial_wait_time
                continue
            except Exception as e:
                logging.error(e)
                logging.warning(f'Error occur while downloading report. : {i}')
                logging.warning(response.text)

        elif response.status_code == 400:
            print(f'Last report: {i}')

        time_use = time.time() - initial_time
        print(f'use {time_use}sec')

        # time.sleep(wait_time)
        await asyncio.sleep(wait_time)
        wait_time = wait_time * wait_time_rate
        if wait_time > max_wait_time:
            wait_time = max_wait_time

client.run(os.getenv('autokulimi-token'))
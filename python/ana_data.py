import json
import time
import logging
import re
import os
from dotenv import load_dotenv
load_dotenv()

# =======Config=======
logging.basicConfig(level=logging.NOTSET)
round = '4'
web_root = os.getenv('web-root')
record_path = os.path.join(web_root, 'ofc', f'{round}.ofc')


# =======Initialize=======
report_line_graph = {}
kill_count = {}
killed_count = {}
weapon_count = {}
hour_count = {}
times_count = {}
damage_count = {}
damaged_count = {}
loot_index = []
xp_count = {}
loot_count = {}
loot_list = {}
weapon_list = []
castle_damage = {}

global_weapon_list = []

match_db = {}
player_db = {}

faction_damage = {}
faction_damaged = {}
faction_times = {}
faction_loot = {}

fighter_faction = {}

faction_list = []

f = open(record_path, 'r', encoding='utf8')
a = f.read().split('\n')
global_kill_count = 0
match_id = 0
print(len(a))

for line in a:
    match_id += 1

    try:
        line_dict = json.loads(line)
    except Exception as e:
        logging.error(e)
        logging.warning(f'error: Can not jsonlize. id: {match_id}')
        logging.warning(line)
        continue

    match_db[match_id] = line_dict

    if match_id != line_dict['report']['id']:
        print(f'{match_id} miss, get {line_dict["report"]["id"]}')
        break

    report_line_graph[str(int((line_dict['report']['time']) / 3600000) * 3600000)] = report_line_graph.get(
        str(int((line_dict['report']['time']) / 3600000) * 3600000), 0) + 1
    if line_dict['report']['aFactionName'] not in faction_list: faction_list.append(line_dict['report']['aFactionName'])
    if line_dict['report']['bFactionName'] not in faction_list: faction_list.append(line_dict['report']['bFactionName'])

    times_count[line_dict['report']['aName']] = times_count.get(line_dict['report']['aName'], 0) + 1
    times_count[line_dict['report']['bName']] = times_count.get(line_dict['report']['bName'], 0) + 1
    if line_dict['report']['location'][:len(line_dict['report']['aFactionName'])] != line_dict['report'][
        'aFactionName']:
        faction_times[line_dict['report']['aFactionName']] = faction_times.get(line_dict['report']['aFactionName'],
                                                                               0) + 1
    for fighter in line_dict['report']['messages']['stats']:
        player_db[line_dict['report']['messages']['stats'][fighter]['name']] = line_dict['report']['messages']['stats'][fighter]
        player_db[line_dict['report']['messages']['stats'][fighter]['name']]['faction'] = line_dict['report'][f'{fighter}FactionName']

    for message in line_dict['report']['messages']['messages']:

        if message.get('s') == 'critical' and '被擊殺身亡了，' in message['m']:
            killed_name, kill_name = (line_dict['report']['aName'], line_dict['report']['bName']) if \
                message['m'].split('被擊殺身亡了，')[0] == line_dict['report']['aName'] else (
                line_dict['report']['bName'], line_dict['report']['aName'])
            if kill_name in kill_count:
                kill_count[kill_name] += 1
            else:
                kill_count[kill_name] = 1
            if killed_name in killed_count:
                killed_count[killed_name] += 1
            else:
                killed_count[killed_name] = 1

        if message['m'][-3:] == '點傷害':
            p = re.compile(r'\d+')

            if message['m'][:len(line_dict['report']['aName'])] == line_dict['report']['aName']:
                if line_dict['report']['bName']:
                    damage_count[line_dict['report']['aName']] = damage_count.get(line_dict['report']['aName'],
                                                                                  0) + int(p.findall(message['m'])[-1])
                    damaged_count[line_dict['report']['bName']] = damaged_count.get(line_dict['report']['bName'],
                                                                                    0) + int(
                        p.findall(message['m'])[-1])
                    faction_damage[line_dict['report']['aFactionName']] = faction_damage.get(
                        line_dict['report']['aFactionName'], 0) + int(p.findall(message['m'])[-1])
                    faction_damaged[line_dict['report']['bFactionName']] = faction_damage.get(
                        line_dict['report']['bFactionName'], 0) + int(p.findall(message['m'])[-1])
                else:
                    castle_damage[line_dict['report']['aName']] = castle_damage.get(line_dict['report']['aName'],
                                                                                    0) + int(
                        p.findall(message['m'])[-1])
            else:
                damage_count[line_dict['report']['bName']] = damage_count.get(line_dict['report']['bName'], 0) + int(
                    p.findall(message['m'])[-1])
                damaged_count[line_dict['report']['aName']] = damaged_count.get(line_dict['report']['aName'], 0) + int(
                    p.findall(message['m'])[-1])
                faction_damage[line_dict['report']['bFactionName']] = faction_damage.get(
                    line_dict['report']['bFactionName'], 0) + int(p.findall(message['m'])[-1])
                faction_damaged[line_dict['report']['aFactionName']] = faction_damaged.get(
                    line_dict['report']['aFactionName'], 0) + int(p.findall(message['m'])[-1])

    for message in line_dict['report']['messages']['messages']:
        if message.get('s') == 'info' and message['m'][-4:] == '點經驗值':
            xp_count[message['m'].split('獲得了')[-2]] = xp_count.get(message['m'].split('獲得了')[-2], 0) + int(
                message['m'].split(' ')[-2])

    for message in line_dict['report']['messages']['messages']:
        if message.get('s') == 'critical' and message['m'][:3] == '獲得了':
            loot_list[message['m'].split(' ')[3]] = loot_list.get(message['m'].split(' ')[3],
                                                                  {'floor': message['m'].split(' ')[1]})
            loot_count[line_dict['report']['aName']] = loot_count.get(line_dict['report']['aName'], [
                f"{line_dict['report']['bFactionName']}第{message['m'].split(' ')[1]}層：{message['m'].split(' ')[3]}"]) + [
                                                           f"{line_dict['report']['bFactionName']}第{message['m'].split(' ')[1]}層：{message['m'].split(' ')[3]}"]
            if message['m'].split(' ')[3] not in loot_index: loot_index.append(message['m'].split(' ')[3])
            faction_loot[line_dict['report']['aFactionName']] = faction_loot.get(line_dict['report']['aFactionName'],
                                                                                 []) + [
                                                                    f"{line_dict['report']['bFactionName']}第{message['m'].split(' ')[1]}層：{message['m'].split(' ')[3]}"]
            break

    this_hour = time.localtime(int(line_dict['report']['time']) / 1000).tm_hour
    hour_count[this_hour] = hour_count.get(this_hour, 0) + 1

    for weapon in line_dict['report']['messages']['stats']['a']['equipments']:
        weapon_count[weapon['type']] = weapon_count.get(weapon['type'], 0) + 1
        global_weapon_list.append(weapon)

    for weapon in line_dict['report']['messages']['stats'].get('b', {}).get('equipments', []):
        weapon_count[weapon.get('type')] = weapon_count.get(weapon.get('type'), 0) + 1
        global_weapon_list.append(weapon)

hour_count_list = [0 for i in range(24)]

for i in range(0, 24):
    hour_count_list[i] = hour_count[i]

# =======Generate JSON file=======

with open(os.path.join(web_root, round, 'CastleDamage.json'), 'w', encoding='utf8') as f:
    f.write(str(sorted(castle_damage.items(), key=lambda x: x[1], reverse=True)))

with open(os.path.join(web_root, round, 'Damage.json'), 'w', encoding='utf8') as f:
    f.write(str(sorted(damage_count.items(), key=lambda x: x[1], reverse=True)))

with open(os.path.join(web_root, round, 'Damaged.json'), 'w', encoding='utf8') as f:
    f.write(str(sorted(damaged_count.items(), key=lambda x: x[1], reverse=True)))

with open(os.path.join(web_root, round, 'Faction12.json'), 'w', encoding='utf8') as f:
    f.write(str(sorted(faction_list)))

with open(os.path.join(web_root, round, 'Faction1.json'), 'w', encoding='utf8') as f:
    f.write(str(sorted(faction_damage.items())))

with open(os.path.join(web_root, round, 'Faction2.json'), 'w', encoding='utf8') as f:
    faction_exp = {}
    for fighter in player_db:
        faction_exp[player_db[fighter]['faction']] = faction_exp.get(player_db[fighter]['faction'], 0) + player_db[fighter]['fightExp']
    f.write(str(sorted(faction_exp.items())))

with open(os.path.join(web_root, round, 'Faction3.json'), 'w', encoding='utf8') as f:
    f.write(str(sorted(faction_times.items(), key=lambda x: x[1], reverse=True)))

with open(os.path.join(web_root, round, 'Faction4.json'), 'w', encoding='utf8') as f:
    faction_loot_count = {}
    for faction in faction_loot:
        faction_loot_count[faction] = len(faction_loot[faction])
    f.write(str(sorted(faction_loot_count.items(), key=lambda x: x[1], reverse=True)))

with open(os.path.join(web_root, round, 'Kill.json'), 'w', encoding='utf8') as f:
    f.write(str(sorted(kill_count.items(), key=lambda x: x[1], reverse=True)))

with open(os.path.join(web_root, round, 'Killed.json'), 'w', encoding='utf8') as f:
    f.write(str(sorted(killed_count.items(), key=lambda x: x[1], reverse=True)))

with open(os.path.join(web_root, round, 'Loot.json'), 'w', encoding='utf8') as f:
    f.write(str(sorted(loot_count.items(), key=lambda x: x[1], reverse=True)))

with open(os.path.join(web_root, round, 'laList.json'), 'w', encoding='utf8') as f:
    f.write(str(sorted(loot_list.items(), key=lambda x: x[1], reverse=False)))

with open(os.path.join(web_root, round, 'Report2.json'), 'w', encoding='utf8') as f:
    f.write(str(sorted(hour_count.items(), key=lambda x: x[1], reverse=True)))

with open(os.path.join(web_root, round, 'Report3.json'), 'w', encoding='utf8') as f:
    f.write('[]')

with open(os.path.join(web_root, round, 'Report1.json'), 'w', encoding='utf8') as f:
    f.write(str(hour_count_list))

with open(os.path.join(web_root, round, 'Times.json'), 'w', encoding='utf8') as f:
    f.write(str(sorted(times_count.items(), key=lambda x: x[1], reverse=True)))

with open(os.path.join(web_root, round, 'Weapon1.json'), 'w', encoding='utf8') as f:
    f.write(str([weapon_count[i] for i in weapon_count]))

with open(os.path.join(web_root, round, 'Weapon2.json'), 'w', encoding='utf8') as f:
    f.write(str([i for i in weapon_count]))

with open(os.path.join(web_root, round, 'Weapon3.json'), 'w', encoding='utf8') as f:
    a = 0
    for weapon in global_weapon_list:
        if weapon['name'] in loot_index:
            a += 1
    f.write(str([len(global_weapon_list) - a, a]))

with open(os.path.join(web_root, round, 'Xp.json'), 'w', encoding='utf8') as f:
    f.write(str(sorted(xp_count.items(), key=lambda x: x[1], reverse=True)))

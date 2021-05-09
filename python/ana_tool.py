import json
import re


def dict_jsonlize(my_dict):
    return json.dumps(my_dict, ensure_ascii=False)


def ana_report(ofc_db, report):
    dead = []
    spe = ''
    remarks = '衛兵' if report['report']['location'][:len(report['report']['aFactionName'])] == report['report'][
        'aFactionName'] and \
                      report['report']['messages']['stats']['a'][
                          'role2'] == '衛兵' else ''

    for name in report['report']['messages']['stats']:  # Player initialize
        if report['report']['messages']['stats'][name]['name'] not in ofc_db['player']:
            ofc_db['player'][
                report['report'][name+"Id"]] = {
                'name': report['report']['messages']['stats'][name]['name'],
                'id': report['report'][name+"Id"],
                'role': report['report']['messages']['stats'][name]['role'],
                'role2': report['report']['messages']['stats'][name].get('role2', None),
                'faction': report['report'][name + 'FactionName'],
                'kill': 0,
                'killed': 0,
                'assist': [0, {None}],
                'castleDamage': 0,
                'damage': 0,
                'damaged': 0,
                'report_summary': []
            }

    if report['report']['bName']:  # Count assist
        ofc_db['player'][report['report']['aId']]['assist'][1].add(report['report']['bName'])
        ofc_db['player'][report['report']['bId']]['assist'][1].add(report['report']['aName'])

    for message in report['report']['messages']['messages']:
        if message.get('s') == 'critical' and '被擊殺身亡了，' in message['m']:
            spe = 'kill'
            killed_name, kill_name = (report['report']['aName'], report['report']['bName']) if \
                message['m'].split('被擊殺身亡了，')[0] == report['report']['aName'] else (
                report['report']['bName'], report['report']['aName'])
            killed_id, kill_id = (report['report']['aId'], report['report']['bId']) if \
                message['m'].split('被擊殺身亡了，')[0] == report['report']['aName'] else (
                report['report']['bId'], report['report']['aId'])
            dead.append(killed_name)
            for player in ofc_db['player']:
                if kill_name == player:
                    ofc_db['player'][kill_id]['kill'] += 1
                else:
                    if killed_name in ofc_db['player'][player]['assist'][1]:
                        ofc_db['player'][player]['assist'][1].remove(killed_name)
                        ofc_db['player'][player]['assist'][0] += 1
            ofc_db['player'][killed_id]['killed'] += 1

        if message['m'][-3:] == '點傷害':
            p = re.compile(r'\d+')
            if message['m'][:len(report['report']['aName'])] == report['report']['aName']:
                if report['report']['bName']:
                    ofc_db['player'][report['report']['aId']]['damage'] += int(p.findall(message['m'])[-1])
                    ofc_db['player'][report['report']['bId']]['damaged'] += int(p.findall(message['m'])[-1])
                else:
                    ofc_db['player'][report['report']['aId']]['castleDamage'] += int(p.findall(message['m'])[-1])
                    remarks = f'城牆受到了 {p.findall(message["m"])[-1]} 點傷害'
            else:
                ofc_db['player'][report['report']['bId']]['damage'] += int(p.findall(message['m'])[-1])
                ofc_db['player'][report['report']['aId']]['damaged'] += int(p.findall(message['m'])[-1])
        # if message.get('s') == 'info' and message['m'][-4:] == '點經驗值':
        #     xp_count[message['m'].split('獲得了')[-2]] = xp_count.get(message['m'].split('獲得了')[-2], 0) + int(
        #         message['m'].split(' ')[-2])
        if message.get('s') == 'critical' and message['m'][:3] == '獲得了':
            spe = 'loot'
            ofc_db['loot'].append(message['m'].split(' ')[3])
        if message['m'].split(' ')[0][-1 * len('在攻城過程中消耗了'):] == '在攻城過程中消耗了':
            if int(message['m'].split(' ')[1]) > report['report']['messages']['stats']['a']['hp']:
                dead.append(report['report']['aName'])
        if message.get('s') == 'critical' and message['m'].split(' ')[0] == '第' and message['m'].split(' ')[-1] == '層被摧毀了':
            spe = 'floor'
            remarks = message['m']

    ofc_db['report_list'].append({
        "atk_f": report['report']['aFactionName'],
        "def_f": report['report']['bFactionName'],
        "atk_name": report['report']['aName'],
        "atk_id": report['report']['aId'],
        "def_name": report['report']['bName'],
        "def_id": report['report']['bId'],
        "dead": dead,
        "remarks": remarks,
        "time": report['report']['time'],
        "id": report['report']['id']
    })

    for name in report['report']['messages']['stats']:  # Player report summary list.
        ofc_db["player"][report['report'][name+"Id"]]['report_summary'].append({
            "atk_f": report['report']['aFactionName'],
            "def_f": report['report']['bFactionName'],
            "atk_name": report['report']['aName'],
            "atk_id": report['report']['aId'],
            "def_name": report['report']['bName'],
            "def_id": report['report']['bId'],
            "dead": dead,
            "spe": spe,
            "floor": '衛兵' if remarks == '衛兵' else '',
            "time": report['report']['time'],
            "id": report['report']['id']
        })

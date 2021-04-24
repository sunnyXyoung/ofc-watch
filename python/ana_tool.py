import json
import re


def dict_jsonlize(my_dict):
    return json.dumps(my_dict, ensure_ascii=False)


def process_line(ofc_db, report):
    # report_location = report['report']['aFactionName'] if report['report']['location'][:len(report['report']['aFactionName'])] == report['report'][
    #                                                           'aFactionName'] and \
    #                                                       report['report']['messages']['stats']['a'][
    #                                                           'role2'] == '衛兵' else report['report']['bFactionName']

    dead = []
    spe = ''
    remarks = '衛兵' if report['report']['location'][:len(report['report']['aFactionName'])] == report['report'][
        'aFactionName'] and \
                      report['report']['messages']['stats']['a'][
                          'role2'] == '衛兵' else ''

    # if ofc_db['startTime'] == 0:
    #     ofc_db['startTime'] = report['report'][
    #         'time']
    #     ofc_db['initCastle'] = \
    #     global_match_count[report_location]['castle_status']
    #     ofc_db['finalCastle'] = \
    #         global_match_count[report_location]['castle_status']

    for name in report['report']['messages']['stats']:  # Player initialize
        if report['report']['messages']['stats'][name]['name'] not in \
                ofc_db['player']:
            ofc_db['player'][
                report['report']['messages']['stats'][name]['name']] = {
                'name': report['report']['messages']['stats'][name]['name'],
                'role': report['report']['messages']['stats'][name]['role'],
                'role2': report['report']['messages']['stats'][name].get('role2', None),
                'faction': report['report'][name + 'FactionName'],
                'kill': 0,
                'killed': 0,
                'assist': [0, {None}],
                'castleDamage': 0,
                'damage': 0,
                'damaged': 0
            }

    if report['report']['bName']:  # Count assist
        ofc_db['player'][report['report']['aName']]['assist'][1].add(report['report']['bName'])
        ofc_db['player'][report['report']['bName']]['assist'][1].add(report['report']['aName'])

    for message in report['report']['messages']['messages']:
        # message_list = message['m'].split(' ')
        # try:
        #     castle_status = [message_list.pop(1), message_list.pop(2)]
        # 
        #     if message_list == ['第', '層還有', '點血量']:
        #         ofc_db['finalCastle'] = \
        #             castle_status
        #         global_match_count[report_location]['castle_status'] = castle_status
        # except IndexError:
        #     pass
        if message.get('s') == 'critical' and '被擊殺身亡了，' in message['m']:
            spe = 'kill'
            killed_name, kill_name = (report['report']['aName'], report['report']['bName']) if \
                message['m'].split('被擊殺身亡了，')[0] == report['report']['aName'] else (
                report['report']['bName'], report['report']['aName'])
            dead.append(killed_name)
            player = ''
            for player in ofc_db['player']:

                if kill_name == player:

                    ofc_db['player'][kill_name][
                        'kill'] = \
                    ofc_db['player'][kill_name][
                        'kill'] + 1
                    pass
                else:
                    if killed_name in \
                            ofc_db['player'][
                                player]['assist'][1]:
                        ofc_db['player'][
                            player]['assist'][1].remove(killed_name)
                        ofc_db['player'][
                            player]['assist'][0] += 1

            ofc_db['player'][
                killed_name]['killed'] += 1

        if message['m'][-3:] == '點傷害':
            p = re.compile(r'\d+')
            if message['m'][:len(report['report']['aName'])] == report['report']['aName']:
                if report['report']['bName']:
                    ofc_db['player'][report['report']['aName']]['damage'] += int(p.findall(message['m'])[-1])
                    ofc_db['player'][report['report']['bName']]['damaged'] += int(p.findall(message['m'])[-1])
                else:
                    ofc_db['player'][report['report']['aName']]['castleDamage'] += int(p.findall(message['m'])[-1])
                    remarks = f'城牆受到了 {p.findall(message["m"])[-1]} 點傷害'
            else:
                ofc_db['player'][report['report']['bName']]['damage'] += int(p.findall(message['m'])[-1])
                ofc_db['player'][report['report']['aName']]['damaged'] += int(p.findall(message['m'])[-1])
        # if message.get('s') == 'info' and message['m'][-4:] == '點經驗值':
        #     xp_count[message['m'].split('獲得了')[-2]] = xp_count.get(message['m'].split('獲得了')[-2], 0) + int(
        #         message['m'].split(' ')[-2])
        if message.get('s') == 'critical' and message['m'][:3] == '獲得了':
            spe = 'loot'
            for weapon in ofc_db["laList"]:
                if weapon['name'] == message['m'].split(' ')[3]:
                    weapon['owner'] = report['report']['aName']
                    ofc_db['loot'].append(weapon)
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
        ofc_db["player"][report['report']['messages']['stats'][name]['name']]['report_summary'].append({
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
            "id": report['report']['id'],
            "match_id": ofc_db['id']
        })

    # print(report['report']['time'] - ofc_db[
    #     'endTime'])

    # the match end
    # print("endtime", ofc_db['endTime'])
    # if (report['report']['time']) - ofc_db[
    #     'endTime'] > (match_determinate_time * 1000):
    #     for player in ofc_db['player']:
    #         ofc_db['player'][player]['assist'] = \
    #         ofc_db['player'][player]['assist'][
    #             0]
    #         if ofc_db['player'][player][
    #             'faction'] == report_location:
    #             ofc_db['def_player'].append(
    #                 ofc_db['player'][player])
    #         else:
    #             ofc_db['atk_player'].append(
    #                 ofc_db['player'][player])
    #
    #     global_match_count[report_location]['count'] += 1

        # Initialize new match.
        # ofc_db = {
        #     "startTime": 0,
        #     "endTime": 9999999999999,
        #     "location": report_location,
        #     "initCastle": global_match_count[report_location]['castle_status'],
        #     "finalCastle": global_match_count[report_location]['castle_status'],
        #     "id": f'{report_location}_{str(global_match_count[report_location]["count"]).zfill(3)}',
        #     "loot": [],
        #     "player": {},
        #     "atk_player": [],
        #     "def_player": [],
        #     "report_list": [],
        # }
        # {
        #     'id': f'{report_location}_{str(global_match_count[report_location]["count"]).zfill(3)}',
        #
        # }
        # global_match_count[report_location]['count'] += 1
        # ofc_db = {
        #
        # }
    # else:
    #     ofc_db['endTime'] = report['report'][
    #         'time']
        # print(ofc_db['endTime'])

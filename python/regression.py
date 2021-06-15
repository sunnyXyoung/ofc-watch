import os
from dotenv import load_dotenv
import json
import re
import logging

load_dotenv()
web_root = os.getenv('web-root')
match_dir = os.path.join(web_root, 'ofc')

pass_admin = True

available_round = []

report_list = ['4']
all_round = False
if all_round:
    for directory in os.listdir(match_dir):
        if os.path.isdir(os.path.join(match_dir, directory)):
            available_round.append(directory)

for round_ in available_round:
    for match in os.listdir(os.path.join(match_dir, round_)):
        try:
            with open(os.path.join(match_dir, round_, match), 'r', encoding='utf8') as f:
                report = json.loads(f.read().strip())
        except Exception as e:
            logging.error(e)
            logging.warning(f'Can not jsonlize. file: {round_}/{match}')
            continue

        if report.get('aBadge', {}).get('label') == '茅場' or report.get('bBadge', {}).get('label') == '茅場':
            logging.warning('茅場晶彥 detected.')
            if pass_admin:
                continue

        if report.get('aBadge', {}).get('label') == '神' or report.get('bBadge', {}).get('label') == '神':
            logging.warning('大麻合法化 detected.')
            if pass_admin:
                continue

        report_list.append(report)

data_list = []
# (aExp, aAtk, bExp, bDef, result)

spec_type = '長槍'
spec_role = '戰鬥員'

for report in report_list:
    report = report['report']
    if spec_type:
        if not all((i['type'] == spec_type for i in report['messages']['stats']['a']['equipments'] + report['messages']['stats']['b']['equipments'])):
            continue
    if spec_role:
        if not all((report['messages']['stats'][i]['role'] == spec_role for i in report['messages']['stats'])):
            continue

    for message in report['message']:
        if message['m'][-3:] == '點傷害':
            p = re.compile(r'\d+')
            result = int(p.findall(message['m'])[-1])
            stat = report['messages']['stats']
            if message['m'][:len(report['aName'])] == report['aName']:
                data_list.append((stat['a']['fightExp'], stat['a']['equipments'][0]['atk'], stat['a']['fightExp'], stat['b']['equipments'][0]['def'], result))
            else:
                data_list.append((stat['b']['fightExp'], stat['b']['equipments'][0]['atk'], stat['a']['fightExp'], stat['a']['equipments'][0]['def'], result))

print(data_list)



import os
from dotenv import load_dotenv
import json
import logging

load_dotenv()
web_root = os.getenv('web-root')
match_dir = os.path.join(web_root, 'ofc')

pass_admin = True

available_round = []

report_list = []

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

only_long_gun = []
for report in report_list:
    pass




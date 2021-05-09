import json
import time
import logging
import re
import os
from dotenv import load_dotenv
import sys
import pathlib
import ana_tool

load_dotenv()

# =======Config=======
logging.basicConfig(level=logging.NOTSET)
try:
    round = sys.argv[1]
except IndexError:
    round = '5.5'
web_root = os.getenv('web-root')
record_path = os.path.join(web_root, 'ofc', f'{round}.ofc')

# =======Initialize=======
report_line_graph = {}
floor_line_graph = []
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

faction_list = []

players = {}
player_info = {}
global_match_db = {}


report_check_list = [1 for i in range(len(os.listdir(os.path.join(web_root, 'ofc', round))))]
global_kill_count = 0
match_determinate_time = 600  # sec

ofc_db = {
    "player": {
        1: {
            "name": "Kulimi",
                'role': '',
                'role2': '',
                'faction': '',
                'kill': 0,
                'killed': 0,
                'assist': [0, {None}],
                'castleDamage': 0,
                'damage': 0,
                'damaged': 0
            }
    },
    "player_info": {},
    "global_match_db": {},
    'report_list': [],
    "loot": []
}

for i in range(1, len(os.listdir(os.path.join(web_root, 'ofc', round))) + 1):
    try:
        with open(os.path.join(web_root, 'ofc', round, str(i) + '.json'), 'r', encoding='utf8') as f:
            line_dict = json.loads(f.read().strip())
    except Exception as e:
        logging.error(e)
        logging.warning(f'error: Can not jsonlize. id: {i}')
        # logging.warning(f.read().strip())
        continue

    ana_tool.ana_report(ofc_db, line_dict)

print(ofc_db)

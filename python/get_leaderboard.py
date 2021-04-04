import requests
import time
import os
from dotenv import load_dotenv
import sys
load_dotenv()

try: round = sys.argv[1]
except IndexError: round = '7'
webroot = os.getenv('web-root')

log = open(os.path.join(webroot, 'ofc', f'{round}.leaderboard'), 'a', encoding="utf-8")

leaderboards = ['money', 'fight_exp', 'forge_exp', 'mine_exp', 'kill']

while True:
    headers = {
        'User-Agent': 'I just wanna know all the secret data',
        'Accept': '*/*',
        'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Origin': 'https://ourfloatingcastle.com',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }

    for i in leaderboards:
        response = requests.get(f'https://cache.ourfloatingcastle.com/api/users?order={i}', headers=headers)
        print(response.text)
        log.write(str(time.time()) + ' ' + response.text + '\n')

    time.sleep(10)

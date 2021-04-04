import requests
import time
import os
from dotenv import load_dotenv
import sys
load_dotenv()

try: round = sys.argv[1]
except IndexError: round = '6'
webroot = os.getenv('web-root')

with open(os.path.join(webroot, 'ofc', f'{round}.ofc'), 'r', encoding="utf-8") as log:
    i = len(log.readlines()) + 1

log = open(os.path.join(webroot, 'ofc', f'{round}.ofc'), 'a', encoding="utf-8")

wait_time = 10

while True:
    print(i)
    time1 = time.time()

    headers = {
        'User-Agent': 'I just wanna know all the secret data',
        'Accept': '*/*',
        'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'token': os.getenv('watch-token'),
        'Origin': 'https://ourfloatingcastle.com',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }
    response = requests.get(f'https://api.ourfloatingcastle.com/api/report/{i}', headers=headers)
    print(response.text)

    if '\n' in response.text:
        print(response.text)
        continue

    if response.text == '{"statusCode":400,"message":"戰報不存在"}':
        print(f'lastest match: {i}')
        time.sleep(wait_time)
        wait_time = wait_time * 1.5 + 10
        if wait_time > 600:
            wait_time = 600
    else:
        log.write('\n' + response.text)
        i += 1
        wait_time = 10
        time_use = time.time() - time1
        print(f'use{time_use}sec')

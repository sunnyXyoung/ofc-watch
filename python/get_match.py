import requests
import time
import os
from dotenv import load_dotenv
import sys
import json
import logging
load_dotenv()


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


logging.basicConfig(level=logging.NOTSET)
try: round = sys.argv[1]
except IndexError: round = '6'
webroot = os.getenv('web-root')
initial_wait_time = 10
wait_time = initial_wait_time
wait_time_rate = 1.5
max_wait_time = 600

try: os.mkdir(os.path.join(webroot, 'ofc', round))
except FileExistsError: pass
exist_report = {}
for i in os.listdir(os.path.join(webroot, 'ofc', round)):
    if '.json' in i: exist_report[int(i[:-5])] = i

try:
    for i in range(1, sorted(exist_report.items())[-1]+1):
        if f'{i}.json' != exist_report.get(i, ''):
            with open(os.path.join(webroot, 'ofc', round, f'{i}.json'), 'a', encoding="utf-8") as f:
                f.write(json.dumps(json.loads(get_report(i)), ensure_ascii=False))
    i = sorted(exist_report.items())[-1]
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
            with open(os.path.join(webroot, 'ofc', round, f'{i}.json'), 'a', encoding="utf-8") as f:
                f.write(json.dumps(line_dict, ensure_ascii=False))
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

    time.sleep(wait_time)
    wait_time = wait_time * wait_time_rate
    if wait_time > max_wait_time:
        wait_time = max_wait_time

import os
import time
from dotenv import load_dotenv
import sys
load_dotenv()
try:
    round = sys.argv[1]
except IndexError:
    round = '5.5'
web_root = os.getenv('web-root')
while True:
    os.system(f'python3 python/ana_data.py {round}')
    with open(os.path.join(web_root, "About.json"), 'w', encoding='utf8') as f:
        result = time.localtime(time.time())
        f.write(f'["{result.tm_year}/{result.tm_mon}/{result.tm_mday} {str(result.tm_hour).zfill(2)}:{str(result.tm_min).zfill(2)}:{str(result.tm_sec).zfill(2)}]')
    time.sleep(60)

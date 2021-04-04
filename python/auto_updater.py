import os
import time
from dotenv import load_dotenv
load_dotenv()

web_root = os.getenv('web-root')
while True:
    os.system('python3 python/ana_data.py 6')
    with open(os.path.join(web_root, "About.json"), 'w', encoding='utf8') as f:
        result = time.localtime(time.time())
        f.write(f'["{result.tm_year}/{result.tm_mon}/{result.tm_mday} {result.tm_hour}:{result.tm_min}:{result.tm_sec}   版本：1.0.4"]')
    time.sleep(600)

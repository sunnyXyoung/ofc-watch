import os
from dotenv import load_dotenv
import sys
import json
import logging
load_dotenv()

rounds = ['4', '5', '6']
webroot = os.getenv('web-root')

for round in rounds:
    with open(os.path.join(webroot, 'ofc', f'{round}.ofc')) as f:
        for i in f.readlines():
            with open(os.path.join(webroot, 'ofc', round, f'{json.loads(i.strip())["report"]["id"]}.json'), 'a', encoding="utf-8") as f:
                f.write(i.strip())

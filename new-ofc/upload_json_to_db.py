import pymongo
import sys
import os
import json
from dotenv import load_dotenv
load_dotenv()


_round = sys.argv[1]
mgclient = pymongo.MongoClient(os.getenv('dbconnect'))
webroot = os.getenv('web-root')

ofc_db = mgclient[f'ofc{_round}']
report_collection = ofc_db['report']

for i in os.listdir(os.path.join(webroot, 'ofc', _round)):
	with open(os.path.join(webroot, 'ofc', _round, i), 'r') as f:
		report = json.load(f)
		report['_id'] = report['report']['id']
		if report['report']['id'] % 100 == 0:
			print(report['report']['id'])
print(f'done, total {len(os.listdir(os.path.join(webroot, 'ofc', _round)))} reports')



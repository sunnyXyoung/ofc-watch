import requests
import time

import random



log = open('history_fight.txt', 'a', encoding="utf-8")
time_use = 0
i = 37904
while True:
	i += 1
	time1 = time.time()
	# time.sleep((0.25 if 0.25-time_use < 0 else 0.25-time_use) + random.random()/4)
	headers = {
	    'User-Agent': 'I just wanna know all the special weapon',
	    'Accept': '*/*',
	    'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
	    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50Ijp7ImVtYWlsIjoiaWFsaWF4aW1pbHVrQGdtYWlsLmNvbSIsInVzZXJJZCI6NzQzM30sInYiOjQsImlhdCI6MTYxNDE3NzI2MSwiZXhwIjoxNjI5NzI5MjYxfQ.-kT6RsBRWK9u7cNuggfXNMxi3XIojBE72ctH8BUiMzM',
	    'Origin': 'https://ourfloatingcastle.com',
	    'Connection': 'keep-alive',
	    'TE': 'Trailers',
	}
	

	response = requests.get(f'https://api.ourfloatingcastle.com/api/report/{i}', headers=headers)

	print(response.text)
	break

	if response.text == '{"statusCode":400,"message":"戰報不存在"}':
		print(f'lastest match: {i}')
		time.sleep(3600)
		
	else:
		log.write(response.text+'\n')
	
		time_use = time.time() - time1
		print(f'use{time_use}sec')
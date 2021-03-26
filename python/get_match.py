import requests
import time

round = '6'


with open(f'history_{round}.txt', 'r', encoding="utf-8") as log:
	i = len(log.readlines())+1

log = open(f'history_{round}.txt', 'a', encoding="utf-8")


while True:
	print(i)
	time1 = time.time()

	headers = {
	    'User-Agent': 'I just wanna know all the secret data',
	    'Accept': '*/*',
	    'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
	    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50Ijp7ImVtYWlsIjoidHBpcmNzYXZhajAxQGdtYWlsLmNvbSIsInVzZXJJZCI6NDkxOH0sInYiOjYsImlhdCI6MTYxNjc0NDc3OCwiZXhwIjoxNjMyMjk2Nzc4fQ.-ZY9URncV9IY4srCmnwvSyw4VXyajUQi_9qubqrTdnA',
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
		time.sleep(3600)
		
	else:
		log.write('\n' + response.text)
		i += 1
	
		time_use = time.time() - time1
		print(f'use{time_use}sec')



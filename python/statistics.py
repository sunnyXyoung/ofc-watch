import json
import time
import matplotlib.pyplot as plt


f = open('history_five.txt', 'r', encoding='utf8')


weapon_count = {}
hour_count = {}

a = f.read().split('\n')

a.pop()

last_number = 0
print(len(a))


for line in a:

	
	try:
		line_dict = json.loads(line)
	except:
		print(line)
		print('error cuuro', last_number+1)
		continue


	if last_number + 1 != line_dict['report']['id']:
		print(f'{last_number + 1} miss')
		break
	else:
		last_number = line_dict['report']['id']

	this_hour = time.localtime(int(line_dict['report']['time'])/1000).tm_hour

	try:
		hour_count[this_hour] += 1
	except:
		hour_count[this_hour] = 1

	# for weapon in line_dict['report']['messages']['stats']['a']['equipments']:

	
	
print(weapon_count)
print(last_number)

print(hour_count)

hour_count_list = [0 for i in range(24)]

for i in range(0, 24):
	hour_count_list[i] = hour_count[i]

print(hour_count_list)


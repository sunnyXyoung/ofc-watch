import json
import time

round = 4

web_root = '/Users/kulimi/ofc-watch/'

f = open('history_fight.txt', 'r', encoding='utf8')

kill_count = {}
killed_count = {}
weapon_count = {}
hour_count = {}

a = f.read().split('\n')



match_id = 0
print(len(a))


for line in a:
	match_id += 1

	try:
		line_dict = json.loads(line)
	except:
		print(line)
		print('error cuuro', match_id)
		continue


	if match_id != line_dict['report']['id']:
		print(f'{match_id} miss, get { line_dict["report"]["id"] }')
		break

	this_hour = time.localtime(int(line_dict['report']['time'])/1000).tm_hour

	try:
		hour_count[this_hour] += 1
	except:
		hour_count[this_hour] = 1

	for weapon in line_dict['report']['messages']['stats']['a']['equipments']:
		try:	
			weapon_count[weapon['type']] += 1
		except:
			weapon_count[weapon['type']] = 1


	try:
		for weapon in line_dict['report']['messages']['stats']['b']['equipments']:
			try:
				weapon_count[weapon['type']] += 1
			except:
				weapon_count[weapon['type']] = 1
	except:
		pass

	
	
print(weapon_count)

print(hour_count)

hour_count_list = [0 for i in range(24)]

for i in range(0, 24):
	hour_count_list[i] = hour_count[i]

print(hour_count_list)



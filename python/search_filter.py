import discord
import datetime

def winner_and_loser(report_dict):
	for m in report_dict['messages']['messages']:
		if m.get('s') == 'critical' and m['m'].startswith(f"{report_dict.get('bName', '')}被擊殺身亡了，{report_dict['aName']}還有") and m['m'].endswith("點體力"):
			return ('a', 'b')
		elif m.get('s') == 'critical' and m['m'].startswith(f"{report_dict['aName']}被擊殺身亡了，{report_dict.get('bName', '')}還有") and m['m'].endswith("點體力"):
			return ('b', 'a')
		elif m.get('s') == 'info' and m['m'].startswith(f"{report_dict['bName']}被打得落荒而逃了，{report_dict['aName']}還有") and m['m'].endswith('點體力'):
			return ('a', 'b')
	return ('', '')


def report_to_embed(report, _round, footer_text):
	report_dict = report['report']
	for faction in [report_dict["aFactionName"], report_dict["bFactionName"]]:
		if report_dict['location'].startswith(faction):
			break
	else:
		print(report_dict['location'], [report_dict["aFactionName"], report_dict["bFactionName"]])
				
	summary = '戰報'
	i = report_dict['id']

	for m in report_dict['messages']['messages']:
		a = m['m'].split(' ')
		try:
			if m.get('s') == 'critical' and ((m['m'].startswith(f"{report_dict['aName']}被擊殺身亡了，{report_dict.get('bName', '')}還有") and m['m'].endswith("點體力")) or (m['m'].startswith(f"{report_dict.get('bName', '')}被擊殺身亡了，{report_dict['aName']}還有") and m['m'].endswith("點體力"))) and faction == report_dict['aFactionName']:
				summary = '[衛兵] ' + m['m']
			if m.get('s') == 'critical' and ((m['m'].startswith(f"{report_dict['aName']}被擊殺身亡了，{report_dict.get('bName', '')}還有") and m['m'].endswith("點體力")) or (m['m'].startswith(f"{report_dict.get('bName', '')}被擊殺身亡了，{report_dict['aName']}還有") and m['m'].endswith("點體力"))):
				summary = m['m']
				break
			elif m.get('s') == 'critical' and a[:-1] == f"獲得了{report_dict['location'][len(faction):]}獎勵".split(' '):
				summary = m['m']
				break
			elif m.get('s') == 'critical' and m['m'] == f"{report_dict['location'][len(faction):]}被摧毀了":
				summary = m['m']
				break
			elif m['m'].startswith(f'{report_dict["aName"]}直接攻擊城堡，造成') and m['m'].endswith('點傷害'):
				summary = m['m']
				break
			elif m.get('s') == 'info' and m['m'].startswith('雙方大戰 16 回合不分勝負！'):
				summary = m['m']
				break
			elif m.get('s') == 'info' and m['m'].startswith(f"{report_dict['bName']}被打得落荒而逃了，{report_dict['aName']}還有") and m['m'].endswith('點體力'):
				summary = m['m']
				break
		except IndexError:
			pass


	t = discord.Embed(title=summary, description=f"在 **{report_dict['location']}**", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcfromtimestamp(report_dict['time'] / 1000))
	t.set_author(name=f"戰報編號{i}", url=f"https://ofc-watch.kulimi.tw/history/{_round}/{i}")

	equip_list = '\n'.join([f"{weapon['quality']}的 **{weapon['name']}**（{weapon['type']}）攻擊{weapon['atk']}、防禦{weapon['def']}、礦力{weapon['minePower']}" for weapon in report_dict['messages']['stats']['a']['equipments']])
	text = f"陣營：**{report_dict['aFactionName']}**\n玩家：**{report_dict['aName']}**\n職業：**{report_dict['messages']['stats']['a']['role']}**\n副職：**{report_dict['messages']['stats']['a'].get('role2', '無')}**\nHP：**{report_dict['messages']['stats']['a']['hp']}**\n熟練：**{report_dict['messages']['stats']['a']['fightExp']}**\nID：**{report_dict['aId']}**\n裝備：\n{equip_list}"
	t.add_field(name="**攻擊方**", value=text, inline=True)
				
	if report_dict.get('bName'):
		equip_list = '\n'.join([f"{weapon['quality']}的 **{weapon['name']}**（{weapon['type']}）攻擊{weapon['atk']}、防禦{weapon['def']}、礦力{weapon['minePower']}" for weapon in report_dict['messages']['stats']['b']['equipments']])
		text = f"陣營：**{report_dict['bFactionName']}**\n玩家：**{report_dict['bName']}**\n職業：**{report_dict['messages']['stats']['b']['role']}**\n副職：**{report_dict['messages']['stats']['b'].get('role2', '無')}**\nHP：**{report_dict['messages']['stats']['b']['hp']}**\n熟練：**{report_dict['messages']['stats']['b']['fightExp']}**\nID：**{report_dict['bId']}**\n裝備：\n{equip_list}"
	else:
		text = report_dict['location'] + '的城牆'
	t.add_field(name="**防守方**", value=text, inline=True)

	t.set_footer(text=footer_text)
	return t.copy()



def p(report_dict, test_payload):
	report_dict = report_dict['report']
	print(test_payload in report_dict.get('bName', ''))
	print(test_payload, report_dict.get('bName', ''))
	return test_payload in report_dict['aName'] or test_payload in report_dict.get('bName', '')


def r(report_dict, test_payload):
	report_dict = report_dict['report']
	return test_payload in report_dict['messages']['stats']['a']['role'] or test_payload in report_dict['messages']['stats'].get('b', {}).get('role', '')


def r2(report_dict, test_payload):
	report_dict = report_dict['report']
	return test_payload in report_dict['messages']['stats']['a']['role2'] or test_payload in report_dict['messages']['stats'].get('b', {}).get('role2', '')


def l(report_dict, test_payload):
	report_dict = report_dict['report']
	return test_payload in report_dict['location']


def w(report_dict, test_payload):
	report_dict = report_dict['report']
	return any([test_payload in w['type'] for w in (report_dict['messages']['stats']['a']['equipments'] + report_dict['messages']['stats'].get('b', {}).get('equipments', []))])


def wn(report_dict, test_payload):
	report_dict = report_dict['report']
	return any([test_payload in w['name'] for w in (report_dict['messages']['stats']['a']['equipments'] + report_dict['messages']['stats'].get('b', {}).get('equipments', []))])


def f(report_dict, test_payload):
	report_dict = report_dict['report']
	return test_payload == report_dict['aFactionName'] or test_payload == report_dict['bFactionName']


def s(report_dict, test_payload):
	report_dict = report_dict['report']
	return test_payload in str(report_dict)


def Wp(report_dict, test_payload):
	report_dict = report_dict['report']
	w = winner_and_loser(report_dict)[0]
	return test_payload in report_dict.get(w+'Name')


def Wr(report_dict, test_payload):
	report_dict = report_dict['report']
	w = winner_and_loser(report_dict)[0]
	return test_payload in report_dict['messages']['stats'].get(w, {}).get('role', '')


def Wr2(report_dict, test_payload):
	report_dict = report_dict['report']
	w = winner_and_loser(report_dict)[0]
	return test_payload in report_dict['messages']['stats'].get(w, {}).get('role2', '')


def Ww(report_dict, test_payload):
	report_dict = report_dict['report']
	w = winner_and_loser(report_dict)[0]
	return any([test_payload in w['type'] for w in report_dict['messages']['stats'].get(winner, {}).get('equipments', [])])


def Wwn(report_dict, test_payload):
	report_dict = report_dict['report']
	winner = winner_and_loser(report_dict)[0]
	return any([test_payload in w['name'] for w in report_dict['messages']['stats'].get(winner, {}).get('equipments', [])])


def Wf(report_dict, test_payload):
	report_dict = report_dict['report']
	w = winner_and_loser(report_dict)[0]
	return test_payload == report_dict.get(w+'FactionName')


def Lp(report_dict, test_payload):
	report_dict = report_dict['report']
	l = winner_and_loser(report_dict)[1]
	return test_payload in report_dict.get(l+'Name')


def Lr(report_dict, test_payload):
	report_dict = report_dict['report']
	l = winner_and_loser(report_dict)[1]
	return test_payload in report_dict['messages']['stats'].get(l, {}).get('role', '')


def Lr2(report_dict, test_payload):
	report_dict = report_dict['report']
	l = winner_and_loser(report_dict)[1]
	return test_payload in report_dict['messages']['stats'].get(l, {}).get('role2', '')


def Lw(report_dict, test_payload):
	report_dict = report_dict['report']
	l = winner_and_loser(report_dict)[1]
	return any([test_payload in w['type'] for w in report_dict['messages']['stats'].get(l, {}).get('equipments', [])])


def Lwn(report_dict, test_payload):
	report_dict = report_dict['report']
	l = winner_and_loser(report_dict)[1]
	return any([test_payload in w['name'] for w in report_dict['messages']['stats'].get(l, {}).get('equipments', [])])


def Lf(report_dict, test_payload):
	report_dict = report_dict['report']
	l = winner_and_loser(report_dict)[1]
	return test_payload == report_dict.get(l+'FactionName')

import os
from dotenv import load_dotenv
import json
import re
import logging

load_dotenv()
web_root = os.getenv('web-root')
match_dir = os.path.join(web_root, 'ofc')

available_round = []

report_list = []
all_round = True
if all_round:
    for directory in os.listdir(match_dir):
        if os.path.isdir(os.path.join(match_dir, directory)):
            available_round.append(directory)

for round_ in available_round:
    print(round_, len(os.listdir(os.path.join(match_dir, round_))))
    for n, match in enumerate(os.listdir(os.path.join(match_dir, round_))):
        try:
            with open(os.path.join(match_dir, round_, match), 'r', encoding='utf8') as f:
                report = json.loads(f.read().strip())
        except Exception as e:
            logging.error(e)
            logging.warning(f'Can not jsonlize. file: {round_}/{match}')
            continue

        report_list.append(report)
        if n % 1000 == 0:
            print(match)

print('done')
data_list = []
# (aExp, aAtk, bExp, bDef, result)

spec_type = '長槍'
spec_role = '戰鬥員'
no_role2 = False

# print(report_list[566])
len_report_list = len(report_list)
for n, report in enumerate(report_list):

    report = report['report']
    if report['bId'] is None:
        continue
    if spec_type:
        if [i['type'] == spec_type for i in report['messages']['stats']['a']['equipments'] + report['messages']['stats']['b']['equipments']] != [True, True]:
            continue
    if no_role2:
        if any([report['messages']['stats'][i].get('role2') for i in report['messages']['stats']]):
            continue

    if spec_role:
        if not all([report['messages']['stats'][i]['role'] == spec_role for i in report['messages']['stats']]):
            continue
        # else:
            # print([report['messages']['stats'][i]['role'] for i in report['messages']['stats']])

    # print('survive check')
    stat = report['messages']['stats']
    for message in report['messages']['messages']:
        if message.get('s'):
            continue

        if message['m'][-6:] == '完全不痛不癢':
            if message['m'][:len(report['aName'])] == report['aName']:
                data_list.append((stat['a']['fightExp'], stat['a']['equipments'][0]['atk'], stat['a']['fightExp'],
                                  stat['b']['equipments'][0]['def'], 0))
            else:
                data_list.append((stat['b']['fightExp'], stat['b']['equipments'][0]['atk'], stat['a']['fightExp'],
                                  stat['a']['equipments'][0]['def'], 0))

        if message['m'][-3:] == '點傷害':
            p = re.compile(r'\d+')
            result = int(p.findall(message['m'])[-1])
            if message['m'][:len(report['aName'])] == report['aName']:
                data = (stat['a']['fightExp'], stat['a']['equipments'][0]['atk'], stat['b']['fightExp'],
                        stat['b']['equipments'][0]['def'], result)
            else:
                data = (stat['b']['fightExp'], stat['b']['equipments'][0]['atk'], stat['a']['fightExp'],
                        stat['a']['equipments'][0]['def'], result)
            data_list.append(data)

    if n % 1000 == 0:
        print(str(int(n / len_report_list * 10000) / 100) + '%')

# for i in data_list:
#     for j in i:
#         print('\t' + str(j), end='')
#     print()

logging.info('total:', len(data_list))
with open('output', 'w') as f:
    for i in data_list:
        for j in i:
            f.write(str(j) + ' ')
        f.write('\n')
logging.info('output file: ./output')
# import numpy as np
# import matplotlib.pyplot as plt
#
# # data = []
# x, y, z = [], [], []
# for i in data_list:
#     # data.append((i[1] - i[3], i[0] - i[2], i[4]))
#     x.append(i[1] - i[3])
#     y.append(i[0] - i[2])
#     z.append(i[4])
# # (攻防差, 熟練差, 結果)
#
#
# ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
# #  将数据点分成三部分画，在颜色上有区分度
# # ax.scatter(x[:10], y[:10], z[:10], c='y')  # 绘制数据点
# # ax.scatter(x[10:20], y[10:20], z[10:20], c='r')
# # ax.scatter(x[30:40], y[30:40], z[30:40], c='g')
# ax.scatter(x[:], y[:], z[:], c='r')
#
# ax.set_zlabel('Z')  # 坐标轴
# ax.set_ylabel('Y')
# ax.set_xlabel('X')
# plt.show()

# (a, b, c, d, y)
# (1*a^1 + 1*b^1)


# import json
#
# f = open('time1.json', 'r')
# a = f.read()
# a = json.loads(a)
# f.close()
# b = []
#
# for i in a:
#     if i[1] == 'Grocery':
#         continue
#     b.append(i)
# print(b)
# f = open('time1.json', 'w')
# f.write(str(b))
# f.close()

f = open('time1.json', 'r')
a = f.read()
f.close()
b = ''
for i in list(a):
    if i == "'":
        i = '"'
    b += i
f = open('time1.json', 'w')
f.write(b)
f.close()
import random
import math as m

relu = lambda a: 1 if a < 1 else a


def bias(arg, dataset='train', batch=32):
    global train_data, validate_data, test_data
    if dataset in ['vali', 'test']:
        o_dataset = validate_data + test_data
    else:
        o_dataset = train_data

    dataset = []
    random.shuffle(o_dataset)
    for i in range(batch):
        dataset.append(o_dataset[i])
    bias_list = []
    for data in dataset:
        try:
            y = arg[0] * m.pow(relu(data[0] - data[2]), arg[1]) * m.pow(relu(data[1] - data[3]), arg[2]) + \
                arg[3] * m.pow(relu(data[2] - data[0]), arg[4]) * m.pow(relu(data[3] - data[1]), arg[5])
        except Exception as e:
            print(e)
            breakpoint()
        bias_list.append(m.pow(y - data[4], 2))

    return abs(sum(bias_list) / len(bias_list))


input_file = 'output'

data_list = []
with open(input_file, 'r') as f:
    for line in f:
        if line:
            data_list.append(tuple(map(int, line.strip().split(' '))))

# print(data_list)


train_data = []
validate_data = []
test_data = []

random.shuffle(data_list)
for n, i in enumerate(data_list):
    if n % 10 == 0:
        validate_data.append(i)
    elif n % 10 == 1:
        test_data.append(i)
    else:
        train_data.append(i)


lr = 0.9

# args = [2.824953606964135, 0.05282675551918997, 0.4743065932426447, 1.0033470792005696, 1.4310862637980297, 0.6166892741405752]
# args = [2.7939200790607743, 0.06928974866266395, 0.43877434972148116, 1.0683662466839614, 1.485649981746621, 0.5938571501086582]  # 300
# a(relu(A-D))^b *(relu(e1-e2))^c + d(relu(D-A))^e *(relu(e2-e1))^f
args = [1.8074152935083114, 0.14629972926184415, 0.4268826081465761, 1, 0.03677117997863281, -0.6175283914570238]
random.shuffle(test_data)

bias_data = {}
for data in test_data + validate_data + train_data:
    arg = args
    y = arg[0] * m.pow(relu(data[0] - data[2]), arg[1]) * m.pow(relu(data[1] - data[3]), arg[2]) + \
        arg[3] * m.pow(relu(data[2] - data[0]), arg[4]) * m.pow(relu(data[3] - data[1]), arg[5])
    b = y - data[4]
    bias_data[int(b)] = bias_data.get(int(b), 0) + 1

b_list = sorted(bias_data)
times_list = []

for b in b_list:
    times_list.append(bias_data[b])


import matplotlib.pyplot as plt
plt.plot(b_list, times_list)
plt.show()

breakpoint()

epoch = 10000
guess_num = 100
guess_range = 0.005

train = False

if train:
    for epoch_count in range(epoch):
        for n, i in enumerate(args):
            result = []
            arg_guess = [args[n]]
            for _ in range(guess_num):
                arg_guess.append(args[n] + (2 * guess_range * random.random() - guess_range))
            for j in arg_guess:
                args2 = [j if m == n else args[m] for m, _ in enumerate(args)]
                result.append(bias(args2))
            args[n] = arg_guess[result.index(min(result))]
        if epoch_count % 10 == 0:
            print(epoch_count, args, bias(args))


print(args)
print(bias(args))
print(bias(args, dataset='test'))
for i in range(20):
    data = random.choice(test_data)
    arg = args
    y = arg[0] * m.pow(relu(data[0] - data[2]), arg[1]) * m.pow(relu(data[1] - data[3]), arg[2]) + \
        arg[3] * m.pow(relu(data[2] - data[0]), arg[4]) * m.pow(relu(data[3] - data[1]), arg[5])
    print(data, y)

breakpoint()



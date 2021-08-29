import random
import math as m


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
        y = arg[0] * m.pow(data[0], arg[1]) + arg[2] * m.pow(data[1], arg[3]) + arg[4] * m.pow(data[2], arg[5]) + arg[6] * m.pow(data[3], arg[7])
        bias_list.append(y - data[4])

    return sum(bias_list) / len(bias_list)


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

args = [1, 1, 1, 1, -1, 1, -1, 1]
# args = [2.0 for i in range(8)]
noise_args = [0, 0, 0, 0, 0, 0, 0, 0]

t1_epoch = 30
t2_epoch = 1000
for epoch_count in range(t1_epoch):

    for n, i in enumerate(args):
        print(epoch_count, n)
        b1 = bias(args)
        args2 = [noise_args[m] if m == n else args[m] for m, _ in enumerate(args)]
        b2 = bias(args2)
        if b1 - b2 == 0:
            continue
        else:
            args[n] = args[n] - (args2[n] - args[n])/(b2 - b1) * b1 * lr


print(args)
print(bias(args))
print(bias(args, dataset='test'))
for i in range(20):
    data = random.choice(test_data)
    arg = args
    y = arg[0] * m.pow(data[0], arg[1]) + arg[2] * m.pow(data[1], arg[3]) + arg[4] * m.pow(data[2], arg[5]) + arg[6] * m.pow(data[3], arg[7])
    print(data, y)

# Will explode, no use.

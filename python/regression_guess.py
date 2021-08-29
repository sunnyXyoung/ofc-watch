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

args = [1, 1, 1, 1, -1, 1, -1, 1]
# args = [2.0 for i in range(8)]

epoch = 10000
guess_num = 10

guess_range = 0.001
a = [1.2888651990613034, 0.4990590944716508, 1.606767034809324, -1.2818963712136153, 0.5968756446348785, 0.5203989935284624, -1.669339091738711, -0.120899381480995]
for i in range(20):
    data = random.choice(test_data)
    arg = a
    y = arg[0] * m.pow(data[0], arg[1]) + arg[2] * m.pow(data[1], arg[3]) + arg[4] * m.pow(data[2], arg[5]) + arg[6] * m.pow(data[3], arg[7])
    print(data, y)
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
    y = arg[0] * m.pow(data[0], arg[1]) + arg[2] * m.pow(data[1], arg[3]) + arg[4] * m.pow(data[2], arg[5]) + arg[6] * m.pow(data[3], arg[7])
    print(data, y)

breakpoint()
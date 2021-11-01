"""
calculator from line
"""
import math


def num_get(lst: list()):
    for el in lis:
        if not el.strip().isdigit():
            print('incorrect input')
            break
    return [int(n.strip()) for n in lst]


def mlt(lst: list()):
    return lst[0] * lst[1]


def n_sum(lst: list()):
    return lst[0] - lst[1]


def div(lst: list()):
    if lst[1] == 0:
        print("can't divide by zero")
    else:
        return lst[0] / lst[1]


print('give the message')
msg = input('>').strip()


lis = msg.split('+')
if len(lis) > 1:
    print(sum(num_get(lis)))

lis = msg.split('*')
if len(lis) > 1:
    # print(mlt(num_get(lis)))
    print(math.prod(num_get(lis)))

lis = msg.split('-')
if len(lis) > 1:
    print(n_sum(num_get(lis)))

lis = msg.split('/')
if len(lis) > 1:
    print(div(num_get(lis)))

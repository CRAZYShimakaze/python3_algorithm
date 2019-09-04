# -*- coding: utf-8 -*-
'''
@Date: 2019-06-26 20:19:22
@Author: CRAZYSHIMAKAZE
'''
number = int(input())
tanxin = [[-float('inf') for i in range(number)]for i in range(number)]
for i in range(int(input())):
    s, t, l = map(int, input().split())
    tanxin[s][t], tanxin[t][s] = l, l
un = [i for i in range(1, number)]
start = 0
all_ = 0
while un:
    min_L = float('inf')
    for item in un:
        if min_L > tanxin[start][item]:
            min_L = tanxin[start][item]
            temp = item
    un.remove(temp)
    start = temp
    all_ += min_L
print(all_+tanxin[start][0])

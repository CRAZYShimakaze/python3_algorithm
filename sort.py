# -*- coding: utf-8 -*-
'''
@Description: 排序算法
@Date: 2019-04-18 18:05:51
@Author: CRAZYShimakaze
'''
def bubble(x):
    for i in range(len(x)-1):
        for j in range(len(x)-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x


def select(x):
    for i in range(len(x)-1):
        max_value = x[0]
        loc = 0
        for j in range(len(x)-i-1):
            if max_value < x[j+1]:
                max_value, loc = x[j+1], j+1
        x[-1-i], x[loc] = x[loc], x[-1-i]
    return x


def insert(x):  # 从后往前进行队列比较
    for i in range(1, len(x)):
        for j in range(i-1, -1, -1):
            if x[j] > x[i]:
                x[j], x[i], i = x[i], x[j], j
            else:
                break
    return x


def quick(x):
    if x == []:
        return x
    cmp = x[-1]
    left, right = [], []
    x.remove(cmp)
    for item in x:
        if item > cmp:
            right.append(item)
        else:
            left.append(item)
    return quick(left) + [cmp] + quick(right)
def quick_std(x):
    def partition(start, end):
        if start < end:
            sort_index = start
            for i in range(start,end):
                if x[i] < x[end]:
                    x[sort_index],x[i] = x[i],x[sort_index]
                    sort_index += 1
            x[end], x[sort_index] = x[sort_index], x[end]
            partition(start, sort_index - 1)
            partition(sort_index + 1, end)
    if len(x) <= 1:
        return x
    partition(0, len(x) - 1)
    return x
a = [1, 22, 4, 62, 73, 5, 257, 12, 45]
x = quick_std(a)
print(x)

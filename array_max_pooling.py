# -*- coding: utf-8 -*-
'''
@Description: 给定一个一维数组和窗口长度，步长为1，求最大池化后的结果
@Date: 2019-04-18 18:05:51
@Author: CRAZYShimakaze
'''
import queue


def max_pooling(array_p, m):
    index_queue = queue.deque()
    max_list = list()
    for i in range(m):
        while (index_queue and array_p[i] >= array_p[index_queue[-1]]):
            index_queue.pop()
        index_queue.append(i)

    for i in range(m, len(array_p)):
        max_list.append(array_p[index_queue[0]])
        while (index_queue and array_p[i] >= array_p[index_queue[-1]]):
            index_queue.pop()
        if (index_queue and i - m >= index_queue[0]):
            index_queue.popleft()
        index_queue.append(i)
    max_list.append(array_p[index_queue[0]])
    return max_list


lis = [5, 4, 3, 2, 8, 2, 2, 2, 11]
print(max_pooling(lis, 4))

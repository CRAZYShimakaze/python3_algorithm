# -*- coding: utf-8 -*-
'''
@Description: 最小编辑距离
@Date: 2019-09-16 22:10:23
@Author: Leetcode
'''


def func(str1, str2):
    n = len(str1)
    m = len(str2)
    if n*m == 0:
        return n+m
    d = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        d[i][0] = i
    for j in range(m+1):
        d[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            left = d[i - 1][j] + 1
            down = d[i][j - 1] + 1
            left_down = d[i - 1][j - 1]
            if str1[i - 1] != str2[j - 1]:
                left_down += 1
            d[i][j] = min(left, down, left_down)
    return d[n][m]


str1 = input()
str2 = input()
print(func(str1, str2))

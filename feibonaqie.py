# -*- coding: utf-8 -*-
'''
@Description:子斐波那契序列的最大长度
@Date: 2019-09-05 20:06:24
@Author: CRAZYShimakaze
'''
def feibonaqie(a, b, num):
    cnt = 0
    while a + b in num:
        cnt += 1
        a,b = b,a+b
    return cnt + 2

num = list(map(int, input().split()))
max_len = -float('inf')
for i in range(len(num)):
    if i == len(num) - max_len:
        break
    for j in range(i + 1, len(num)):
        max_len = max(max_len, feibonaqie(num[i], num[j], num))
        if j == len(num) - max_len + 1:
            break
print(max_len)

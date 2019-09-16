# -*- coding: utf-8 -*-
'''
@Description: 给定一个数n，求(1,n]之间的数分解质因数后共有多少个质数？
例：6
输出7
2:1 3:1 4:2 5:1 6:2
@Date: 2019-09-16 22:11:14
@Author: CRAZYShimakaze
'''

import math


def func(num, dic):
    i = 2
    if dic.get(str(num)):
        return dic.get(str(num))
    while i <= math.ceil(math.sqrt(num)):
        if num % i == 0:
            cnt = dic[str(num//i)]+1
            dic[str(num)] = cnt
            break
        i += 1
    else:
        dic[str(num)] = 1
        cnt = 1
    return cnt


n = int(input())
alll = 0
base = {'2': 1, '3': 1}
for i in range(2, n+1):
    alll += func(i, base)
print(alll)

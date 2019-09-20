# -*- coding: utf-8 -*-
'''
@Description: A、B两个整数序列，从A中取出一个后，再分别从A、B中拿出一个进行相乘，问最坏情况下乘积最大值为多少？
例：2 2
20 18
2 14
输出：252
@Date: 2019-09-20 20:08:03
@Author: CRAZYShimakaze
'''
n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
if len(a) != 2:
    print(max(a[-2]*b[-1], a[1]*b[0], a[-2]*b[0], a[1]*b[-1]))
else:
    print(sorted([a[0] * b[-1], a[0] * b[0], a[1]*b[-1], a[1]*b[0]])[-2])

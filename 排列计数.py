# -*- coding: utf-8 -*-
'''
@Description: 给定一个长度为N-1只包含0、1的序列A，若一个1到N的排列P满足A[i]=0时P[i]<[i]，A[i]=1时P[i]>[i]，则该排列符合要求，求共有多少符合要求的排列？
@Date: 2019-09-08 16:22:47
@Author: CRAZYShimakaze
'''


def dp(index, big, small):
    if big == 0 and small == 0 and index == len(A):
        return 1
    if A[index] == 0:
        if big == 0:
            return 0
        else:
            sum1 = 0
            for j in range(1, big + 1):
                sum1 += dp(index + 1, j - 1, big + small - j)
            return sum1
    else:
        if small == 0:
            return 0
        else:
            sum2 = 0
            for j in range(1, small + 1):
                sum2 += dp(index + 1, big + small - j, j - 1)
            return sum2
N = 4
A = [1, 1, 0]
A = [0, 1, 0]
alll = 0
for k in range(1, N + 1):
    alll += dp(0,N - k, k - 1)
print(alll)


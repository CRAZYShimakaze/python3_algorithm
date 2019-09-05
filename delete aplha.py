# -*- coding: utf-8 -*-
'''
@Description:给定一串字符，每次可同时删除两个不同的单词，如果可以全部删完输出'YES',否则输出'NO'
@Date: 2019-09-05 13:23:55
@Author: CRAZYShimakaze
'''
ci = int(input())
for _ in range(ci):
    N = int(input())
    num = sorted(list(map(int, input().split())))
    nums = 0
    cnt = 1
    max_ = 0
    for item in num:
        if nums == item:
            cnt += 1
        else:
            if max_ < cnt:
                max_ = cnt
            nums = item
            cnt = 1
    max_ = max_ if max_ > cnt else cnt
    if max_>N//2:
        print('NO')
    else:
        print('YES')

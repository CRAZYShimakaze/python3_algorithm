# -*- coding: utf-8 -*-
'''
@Description: 给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
@Date: 2019-09-14 19:35:01
@Author: typingMonkey
'''
from collections import Counter


def frequencySort(s: str) -> str:
    ct = Counter(s)
    return ''.join([c * t for c, t in sorted(ct.items(), key=lambda x: -x[1])])


def frequencySort1(self, s):
    res = ''
    map = {}
    for i in s:
        if i not in map:
            map[i] = 1
        else:
            map[i] += 1
    l = sorted(map.items(), key=lambda x: x[1], reverse=True)
    for v, k in l:
        res += v*k
    return res


frequencySort('aerhaertafgaergRH')

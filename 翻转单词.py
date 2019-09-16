# -*- coding: utf-8 -*-
'''
@Description:给定一个‘.’结尾的字符串，翻转单词的顺序输出并以.结尾
例：i love   you   .
输出：you love i.
@Date: 2019-09-16 20:54:04
@Author: CRAZYShimakaze
'''


import math
s = input()[:-1].split(' ')
print(' '.join([item for item in s[::-1] if item != '']), end='.')

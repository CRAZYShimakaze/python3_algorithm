# -*- coding: utf-8 -*-
'''
@Description: random7生成random10
@Date: 2019-09-05 20:51:08
@Author: CRAZYShimakaze
'''
import random
x = 41
while x>=40:
    x = (random.randint(1, 7)-1) * 7 + random.randint(1, 7)-1
print(x//4+1)
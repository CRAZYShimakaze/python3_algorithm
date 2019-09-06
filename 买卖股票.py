# -*- coding: utf-8 -*-
'''
@Description:给定一个每天的股价序列，不限制买卖次数，每次卖出手续费2元，求最大利润
@Date: 2019-09-04 18:59:35
@Author: CRAZYSHIMAKAZE
'''
INT_MIN = -float('inf')
prices = [1,3,2,8,4,9]
if not prices:
    print(0)
fee = 2
you = INT_MIN
wu = 0
def judge(you, wu, day):
    if day == len(prices)-1:
        return max(wu, you + prices[day] - fee)
    day += 1
    return judge(max(you, wu - prices[day-1]), max(wu, you + prices[day-1] - fee), day)
print(judge(you, wu, 0))
dp_1 = INT_MIN
dp_0 = 0
for day in range(len(prices)):
    dp_1 = max(dp_1, dp_0-prices[day])
    dp_0 = max(dp_0, dp_1+prices[day]-2)
print(dp_0)

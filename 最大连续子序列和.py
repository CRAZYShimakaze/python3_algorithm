# -*- coding: utf-8 -*-
'''
@Description:给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
@Date: 2019-09-14 18:15:23
@Author: CRAZYShimakaze
'''


def maxSubArray(nums) -> int:
    maxx = nums[0]
    summ = 0
    for item in nums:
        summ = summ + item
        if summ > maxx:
            maxx = summ
        if summ < 0:
            summ = 0
    return maxx


maxSubArray([-2, 1])

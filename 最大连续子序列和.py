# -*- coding: utf-8 -*-
'''
@Description:给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
@Date: 2019-09-14 18:15:23
@Author: leichaojian
'''


def maxSubArray(nums):
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i] + nums[i-1])
        return max(nums)


maxSubArray([-2, 1])

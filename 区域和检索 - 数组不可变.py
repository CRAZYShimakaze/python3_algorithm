# -*- coding: utf-8 -*-
'''
@Description: 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
@Date: 2019-09-08 09:50:56
@Author: CRAZYShimakaze
'''


class NumArray:

    def __init__(self, nums):
        if nums == []:
            self.dp = 0
        else:
            self.dp = [nums[0]]
            for j in range(1, len(nums)):
                self.dp.append(self.dp[-1] + nums[j])

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.dp[j]
        elif self.dp == 0:
            return 0
        return self.dp[j]-self.dp[i-1]


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
param_1 = obj.sumRange(2,5)

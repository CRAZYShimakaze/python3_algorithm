# -*- coding: utf-8 -*-
'''
@Date: 2019-06-05 17:32:11
@Author: CRAZYShimakaze
'''
class Solution:
    def rob(self, nums):
        if len(nums) <= 2:
            return max(nums)
        if len(nums) % 2 == 0:
            a = sum(i for i in nums[::2])
            b = sum(i for i in nums[1::2])
            return max(a, b)
        if len(nums) % 2 == 1:
            a = sum(i for i in nums[:-2:2])
            b = sum(i for i in nums[2::2])
            c = sum(i for i in nums[1::2])
            return max(a, b, c)


s = Solution()
print(s.rob([1, 3, 1, 3, 100]))

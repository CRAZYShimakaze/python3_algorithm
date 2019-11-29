# -*- coding: utf-8 -*-
'''
@Description:给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
@Date: 2019-11-29 18:26:47
@Author: CRAZYShimakaze
'''


class Solution:
    def minSubArrayLen(self, s, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        left = 0
        right = 0
        min_v = float('inf')
        al = 0
        while (right < len(nums)):
            al = al+nums[right]
            while (al < s and right+1 < len(nums)):
                right, al = right + 1, al + nums[right + 1]
            if al < s and min_v == float('inf'):
                return 0
            else:
                while(al - nums[left] >= s):
                    left, al = left+1, al - nums[left]
                min_v = min_v if min_v < right - left + 1 else right - left + 1
            right, left, al = right+1, left+1, al-nums[left]
        return min_v


print(Solution().minSubArrayLen(
    213, [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]))

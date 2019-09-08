# -*- coding: utf-8 -*-
'''
@Description: 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
@Date: 2019-09-08 10:03:38
@Author: CRAZYShimakaze
'''


class Solution:
    def rob(self, nums) -> int:
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        a = nums[0]
        b = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp = max(nums[i]+a, b)
            a, b = b, dp
        return dp
Solution().rob([1,2,3,1])

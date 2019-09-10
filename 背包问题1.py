# -*- coding: utf-8 -*-
'''
@Description: 在n个物品中挑选若干物品装入背包，最多能装多满？假设背包的大小为m，每个物品的大小为A[i]
@Date: 2019-09-10 14:06:55
@Author: CRAZYShimakaze
'''
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        dp = [[0 for i in range(m+1)]for j in range(len(A))]
        for i in range(len(A)):
            for j in range(1,m+1):
                if A[i] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i]] + A[i])
        return dp[len(A) - 1][m]


print(Solution().backPack(12,[2, 3, 5, 7]))

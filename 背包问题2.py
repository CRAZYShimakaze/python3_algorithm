# -*- coding: utf-8 -*-
'''
@Description: 在n个物品中挑选若干物品装入背包，最多能装多大价值？假设背包的大小为m，每个物品的大小为A[i]，价值分别为B[i]
@Date: 2019-09-10 14:06:55
@Author: CRAZYShimakaze
'''
class Solution1:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A, B):
        # write your code here
        dp = [[0 for i in range(m+1)]for j in range(len(A))]
        for i in range(len(A)):
            for j in range(A[i], m+1):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i]] + B[i])
        return dp[len(A) - 1][m]


class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    def backPack(self, m, A, V):
        # write your code here
        f = [0 for i in range(m+1)]
        n = len(A)
        for i in range(n):
            for j in range(m, A[i]-1, -1):
                f[j] = max(f[j], f[j-A[i]] + V[i])
        return f[m]

print(Solution().backPack(12, [2, 3, 5, 7], [3, 5, 2, 6]))

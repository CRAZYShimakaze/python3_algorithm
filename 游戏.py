# -*- coding: utf-8 -*-
'''
@Description: n个包含各自关卡和难度的游戏,只能玩k个游戏,获得的快乐为关卡总量乘以玩的游戏的最小难度,求获得的最大快乐。
输入：3 2(游戏数,可玩数)
1 1(关卡数,难度)
2 2
3 3
输出：10
@Date: 2019-09-20 21:48:46
@Author: CRAZYShimakaze
'''
INT_MAX = float('inf')
n, k = map(int, input().split())
game = []
for i in range(n):
    game.append(list(map(int, input().split())))
dp = [[[0, INT_MAX] for i in range(k+1)] for j in range(n)]
for i in range(n):
    for j in range(1, k+1):
        if game[i][1] >= dp[i-1][j-1][1]:
            dp[i][j][0] = max(dp[i-1][j-1][0]+game[i][0]
                              * dp[i-1][j-1][1], dp[i-1][j][0])
            dp[i][j][1] = dp[i-1][j-1][1]
        else:
            dp[i][j][0] = max((dp[i-1][j-1][0]/dp[i-1][j-1]
                               [1]+game[i][0])*game[i][1], dp[i-1][j][0])
            if dp[i][j][0] != dp[i-1][j][0]:
                dp[i][j][1] = game[i][1]
            else:
                dp[i][j][1] = dp[i-1][j-1][1]
print(int(dp[-1][-1][0]))

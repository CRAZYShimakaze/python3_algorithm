# -*- coding: utf-8 -*-
'''
@Description: 给定一个表示分数的非负整数数组。 玩家1从数组任意一端拿取一个分数，随后玩家2继续从剩余数组任意一端拿取分数，然后玩家1拿，……。每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。最终获得分数总和最多的玩家获胜。

给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/predict-the-winner
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
@Date: 2019-09-06 19:41:02
@Author: CRAZYShimakaze
'''
dp = {}
nums = list(map(int, input().split()))


def max_get(i, j):
    n = len(nums)
    if n % 2 == 0 or n == 1:
        return True
    dp = [0] * n
    for i in reversed(range(n)):
        dp[i] = nums[i]
        for j in range(i+1, n):
            dp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1])
    return dp[-1] >= 0


if max_get(0, len(nums)):
    print('Yes')
else:
    print('No')

# -*- coding: utf-8 -*-
'''
@Description: https://leetcode-cn.com/problems/happy-number/
@Date: 2019-06-05 16:57:03
@Author: CRAZYShimakaze
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        alr = [n]
        while (alr[-1] != 1):
            n = sum(int(item)**2 for item in str(n))
            if n in alr:
                return False
            alr.append(n)
        return True


s = Solution()
print(s.isHappy(256))
print(s.isHappy(19))

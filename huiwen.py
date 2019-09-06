# -*- coding: utf-8 -*-
'''
@Description: 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
@Date: 2019-09-06 15:09:14
@Author: CRAZYShimakaze
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = 0
        b = len(str(x))-1
        x_s = str(x)
        while a<b:
            if x_s[a]!=x_s[b]:
                return False
            a += 1
            b -= 1
        else:
            return True
print(Solution().isPalindrome(123321))
print(Solution().isPalindrome(12321))
print(Solution().isPalindrome(12312321))

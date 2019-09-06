# -*- coding: utf-8 -*-
'''
@Description: 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。
如果小数部分为循环小数，则将循环的部分括在括号内。
@Date: 2019-09-06 15:42:48
@Author: 九章算法助教团队
'''


class Solution:
    """
    @param numerator: a integer
    @param denominator: a integer
    @return: return a string
    """

    def fractionToDecimal(self, numerator, denominator):
        # write your code here
        res = ""
        if numerator/denominator < 0:
            res += "-"
        if numerator % denominator == 0:
            return str(numerator/denominator)
        numerator = abs(numerator)
        denominator = abs(denominator)
        res += str(numerator//denominator)
        res += "."
        numerator %= denominator
        i = len(res)
        table = {}
        while numerator != 0:
            if numerator not in table.keys():
                table[numerator] = i
            else:
                i = table[numerator]
                res = res[:i]+"("+res[i:]+")"
                return res
            numerator = numerator*10
            res += str(numerator//denominator)
            numerator %= denominator
            i += 1
        return res
print(Solution().fractionToDecimal(1,7))

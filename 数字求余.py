# -*- coding: utf-8 -*-
'''
@Description: 给定一个包含‘?’的数字，‘?’可被0-9代替，判断共有多少个数能被13除余5？
例：2??
输出 7 
200 213 226 239 252 265 278 291
@Date: 2019-09-15 21:51:59
@Author: CRAZYShimakaze
'''

# 非最优解，复杂度较高


def repl(temp, cnt):
    if cnt == 0:
        if int(temp) % 13 == 5:
            return 1
        else:
            return 0
    count = 0
    for i in range(10):
        count += repl(temp.replace('?', str(i), 1), cnt - 1)
    return count


if __name__ == "__main__":
    s = input()
    start = 0
    cnt = 0
    for item in s:
        if item == '?':
            cnt += 1
    temp = s
    result = repl(temp, cnt)
    print(result % (10**9+7))

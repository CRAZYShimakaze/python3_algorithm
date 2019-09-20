# -*- coding: utf-8 -*-
'''
@Description: 输入k进制的两个数和字符{'+','-','*'},输出运算后k进制的结果。最多为35进制。超出10的数用A、B、C表示。
输入：3
2
10 110 +
8
12332 4674 *
16
A76D 6ACC -
@Date: 2019-09-20 20:43:19
@Author: CRAZYShimakaze
'''


def trans(num, k):
    base = 0
    summ = 0
    for item in num[::-1]:
        if item.isdigit():
            summ += int(item)*k**base
        else:
            summ += (ord(item)-ord('A') + 10)*k**base
        base += 1
    return summ


def untrans(num, k):
    array = ''
    while num >= k:
        if num % k >= 10:
            array += chr(55+num % k)
        else:
            array += str(num % k)
        num //= k
    if num % k >= 10:
        array += chr(55+num % k)
    else:
        array += str(num % k)
    return array[::-1]


N = int(input())
while N != 0:
    N -= 1
    k = int(input())
    a, b, ch = input().split()
    if ch == '+':
        print(untrans(trans(a, k)+trans(b, k), k))
    elif ch == '-':
        print(untrans(trans(a, k)-trans(b, k), k))
    else:
        print(untrans(trans(a, k)*trans(b, k), k))

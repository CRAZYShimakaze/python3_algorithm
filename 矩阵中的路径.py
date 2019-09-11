# -*- coding: utf-8 -*-
'''
@Description: 给定一个存有字符的矩阵和一个字符串，判断矩阵中是否存在一条路径上的字符恰好为给定字符串。
@Date: 2019-09-11 17:15:03
@Author: CRAZYShimakaze
'''


def find(x, y, index):
    if index == len(string):
        return True
    if x < 0 or y < 0 or x > hang or y > lie or string[index] != juzhen[x][y]:
        return False
    if find(x + 1, y, index + 1) or find(x - 1, y, index + 1) or find(x, y + 1, index + 1) or find(x + 1, y - 1, index + 1):
        return True


def solution(boxes, s):
    for i in range(lie):
        for j in range(hang):
            if find(i, j, s):
                return True
    return False


if __name__ == '__main__':
    juzhen = [['a', 'f', 'e', 'w', 'd'],
              ['e', 'd', 'g', 'h', 'j'],
              ['d', 'a', 'h', 'j', 'n'],
              ['r', 'f', 'g', 'h', 'b'],
              ['r', 'c', 'c', 's', 'd']]
    string = 'eghjhs'
    hang = len(juzhen[0])
    lie = len(juzhen)
    print(solution(juzhen, 0))

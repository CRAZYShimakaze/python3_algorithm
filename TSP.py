# -*- coding: utf-8 -*-
'''
@Description:TSP问题
@Date: 2019-06-26 20:19:22
@Author: CRAZYShimakaze
'''


class TSP_Solve():
    def __init__(self,number,tanxin):
        self.min_dist = INT_MAX
        self.un = [i for i in range(1, number)]
        self.start = 0
        self.tanxin = tanxin
        self.dist = 0
    def tanxinTSP(self, tanxin, number):
        all_ = 0
        while self.un:
            min_L = INT_MAX
            for item in self.un:
                if min_L > self.tanxin[self.start][item]:
                    min_L = self.tanxin[self.start][item]
                    temp = item
            if min_L == INT_MAX:
                return -1
            self.un.remove(temp)
            self.start = temp
            all_ += min_L
        if self.tanxin[self.start][0] == INT_MAX:
            return -1
        return all_ + self.tanxin[self.start][0]

    def huisuTSP(self, unc,start=0, dist=0):
        if not unc:
            return min(dist + self.tanxin[start][0],self.min_dist)
        a = INT_MAX
        for item in unc:
            if dist + self.tanxin[start][item] < self.min_dist:
                a = min(a,self.huisuTSP([i for i in unc if i != item], item,dist + self.tanxin[start][item]))
        return a

INT_MAX = float('inf')
number = int(input())
tanxin = [[INT_MAX for i in range(number)] for i in range(number)]
for i in range(int(input())):
    s, t, l = map(int, input().split())
    tanxin[s][t], tanxin[t][s] = l, l
ss = TSP_Solve(number, tanxin)
print('贪心算法：{}'.format(ss.tanxinTSP(tanxin,number)))#局部最优
print('回溯算法：{}'.format(ss.huisuTSP([i for i in range(1, number)])))

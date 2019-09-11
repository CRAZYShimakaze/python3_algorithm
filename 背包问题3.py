# -*- coding: utf-8 -*-
'''
@Description: 给定硬盘大小和内存大小、一系列需求特定硬盘和内存空间且可以服务特定人数的app，判断如何能够装入服务人数总数最多的app？
用例：
15 10 
5,1,1000#2,3,3000#5,2,15000#10,4,16000
output:31000
@Date: 2019-09-11 16:36:45
@Author: CRAZYShimakaze
'''

#通过率90.91%
def solution(total_disk, total_memory, app_list):
    dp = [[[0 for i in range(total_memory+1)]
           for j in range(total_disk+1)]for k in range(len(app_list))]
    # TODO Write your code here
    for i in range(len(app_list)):
        for j in range(total_disk+1):
            for k in range(total_memory+1):
                if app_list[i][0] > j or app_list[i][1] > k:
                    dp[i][j][k] = dp[i-1][j][k]
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-app_list[i][0]][k-app_list[i][1]]+app_list[i][2])
    return dp[-1][-1][-1]

if __name__ == "__main__": 

    input1 = input()
    disk = int(input1.split()[0])
    memory = int(input1.split()[1])
    input2 = input1.split()[2]
    app_list = [[int(j) for j in i.split(',')] for i in input2.split('#')]
    print(solution(disk, memory, app_list))

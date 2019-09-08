# -*- coding: utf-8 -*-
'''
@Description: 给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2)。
@Date: 2019-09-08 10:23:22
@Author: CRAZYShimakaze
'''
class NumMatrix:

    def __init__(self, matrix): 
        if matrix == []:
            self.flag = 0
        else:
            self.flag = 1
            self.mat = matrix
            wid = len(matrix[0])
            hei = len(matrix)
            self.mat.append([0]*(wid+1))
            for i in range(0, hei):
                self.mat[i].append(0)
                for j in range(0, wid):
                    a = matrix[i-1][j]
                    b = matrix[i][j-1] 
                    c = matrix[i-1][j-1]
                    self.mat[i][j] += a + b - c
                    

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.flag == 0:
            return 0
        return self.mat[row2][col2] - self.mat[row2][col1-1] - self.mat[row1-1][col2] + self.mat[row1-1][col1-1]
# Your NumMatrix object will be instantiated and called as such:
matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]

obj = NumMatrix(matrix)
print(obj.sumRegion(2,1,4,3))

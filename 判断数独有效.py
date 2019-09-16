# -*- coding: utf-8 -*-
'''
@Description: 给定一个9*9数独，未填入数字以X代替，判断数独合法性。
@Date: 2019-09-16 22:12:47
@Author: CRAZYShimakaze
'''


def isvalid(sudo):
    rows = [{} for i in range(9)]
    cols = [{} for i in range(9)]
    boxs = [{} for i in range(9)]
    for i in range(9):
        for j in range(9):
            num = sudo[i][j]
            if num != 'X':
                num = int(num)
                box_index = (i//3)*3+j//3
                rows[i][num] = rows[i].get(num, 0)+1
                cols[j][num] = cols[j].get(num, 0)+1
                boxs[box_index][num] = boxs[box_index].get(num, 0)+1
                if rows[i][num] > 1 or cols[j][num] > 1 or boxs[box_index][num] > 1:
                    return False
    return True


sudo = []
for i in range(9):
    sudo.append(input())
print(isvalid(sudo))

# -*- coding: utf-8 -*-
'''
@Description: 给定一个排序好的数组，两个整数 k 和 x，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。如果有两个数与 x 的差值一样，优先选择数值较小的那个数。

示例 1:

输入: [1,2,3,4,5], k=4, x=3
输出: [1,2,3,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-k-closest-elements

@Date: 2019-11-19 18:05:39
@Author: CRAZYShimakaze
'''


class Solution:
    def findClosestElements(self, arr, k, x):
        min_num = float('INF')
        temp = [item for item in arr]
        for i in range(len(temp)):
            temp[i] = abs(temp[i]-x)
            if temp[i] < min_num:
                index = i
                min_num = temp[index]
        left = index-1
        right = index+1
        ar = [arr[index]]
        k -= 1
        while k != 0:
            if left < 0:
                ar.extend(arr[right:right+k])
                return ar
            elif right == len(temp):
                tt = arr[left + 1 - k:left + 1]
                tt.extend(ar)
                return tt
            else:
                if temp[left] <= temp[right]:
                    ar.insert(0, arr[left])
                    left -= 1
                    k -= 1
                else:
                    ar.append(arr[right])
                    right += 1
                    k -= 1
        return ar


print(Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3))

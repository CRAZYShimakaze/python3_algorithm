# -*- coding: utf-8 -*-
'''
@Description:滑动窗口最大值
@Date: 2019-09-04 21:33:59
@Author: CRAZYShimakaze
'''
import queue
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        left = []
        right = []
        max_list = []
        for index,item in enumerate(nums):
            if index%k==0:
                left.append(item)
            else: 
                if left[-1]>=item:
                    left.append(left[-1])
                else:
                    left.append(item)
        for index,item in enumerate(reversed(nums)):
            if index%k==0:
                right.append(item)
            else: 
                if right[-1]>=item:
                    right.append(right[-1])
                else:
                    right.append(item) 
        right.reverse()           
        for i in range(len(nums)-k+1):
            max_list.append(left[i+k-1] if left[i+k-1]>right[i] else right[i])
        return max_list
    def maxandmin(self,nums,window):
        deq = queue.deque()
        max_index = 0
        for i in range(window):
            if deq and deq[0] == i-window:
                deq.popleft()
            while deq and nums[deq[-1]]<nums[i]:
                deq.pop()
            deq.append(i)
            if nums[i]>nums[max_index]:
                max_index = i
        out = [nums[max_index]]
        for i in range(window,len(nums)):
            if deq and deq[0] == i-window:
                deq.popleft()
            while deq and nums[deq[-1]]<nums[i]:
                deq.pop()
            deq.append(i)
            out.append(nums[deq[0]])
        return out         
print(Solution().maxSlidingWindow([1,2,3,4,2,4,54,5,6,4,3],3))
print(Solution().maxandmin([1,2,3,4,2,4,54,5,6,4,3],3))

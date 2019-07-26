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
        
print(Solution().maxSlidingWindow([1,2,3,4,2,4,54,5,6,4,3],3))
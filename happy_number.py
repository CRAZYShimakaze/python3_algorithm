class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        n = sum(list(map(lambda x: int(x)**2, str(n))))
        alr = [n]
        while (alr[-1] != 1):
            n = sum(list(map(lambda x: int(x)**2, str(n))))
            if n in alr:
                return False
            alr.append(n)
        return True


s = Solution()
print(s.isHappy(256))
print(s.isHappy(19))
#https://leetcode-cn.com/problems/happy-number/
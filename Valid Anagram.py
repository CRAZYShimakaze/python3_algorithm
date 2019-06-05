class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = dict()
        tt = dict()
        for item in s:
            if item in ss:
                ss[item] += 1
            else:
                ss[item] = 1
        for item in t:
            if item in tt:
                tt[item] += 1
            else:
                tt[item] = 1
        return True if tt == ss else False
        #return True if sorted(s) == sorted(t) else False


s = Solution()
print(s.isAnagram('paragram', 'rapagram'))

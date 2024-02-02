class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = {}
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        
        for c in t:
            if c in dic:
                if dic[c] == 0: return c
                dic[c] -= 1
            else:
                return c        
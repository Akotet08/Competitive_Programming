class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = list(t)
        for c in s:
            t.remove(c)
        
        return ''.join(t)
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        n = len(x)
        if len(x) == 1: return True

        is_pal = True
        for i in range(n//2):
            if x[i] != x[n-1-i]:
                is_pal = False
                break
        
        return is_pal

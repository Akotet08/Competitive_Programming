class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(sqrt(c))

        while i <= j:
            s = i **2 + j**2
            if s == c:
                return True
            elif s < c:
                i += 1
            else:
                j -= 1
        
        return False
        
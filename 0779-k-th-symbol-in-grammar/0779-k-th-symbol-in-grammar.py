class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        r = k % 2
        prev = self.kthGrammar(n-1, (k + 1)//2)
        
        if (prev == 0 and (r == 0)) or (prev == 1 and  r==1):
            return 1
        elif (prev == 0 and (r == 1)) or (prev == 1 and  r==0):
            return 0
        

        
class Solution:
    def fib(self, n: int) -> int:
        f0 = 0
        f1 = 1

        for _ in range(n):
            n = f0 + f1
            f0 = f1
            f1 = n
        
        return f0
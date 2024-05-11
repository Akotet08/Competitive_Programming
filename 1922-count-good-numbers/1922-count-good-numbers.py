class Solution:
    def pow(self, a, b):
        if b == 0:
            return 1
        val = self.pow(a, b // 2) % 1000000007
        if (b % 2) == 0:
            return (val * val) % 1000000007
        else:
            return (a % 1000000007) * ((val * val) % 1000000007) % 1000000007

    def countGoodNumbers(self, n: int) -> int:
        even = (n + 1) // 2
        odd = n // 2

        val = self.pow(4, odd) % 1000000007
        val_right = self.pow(5, even) % 1000000007

        return (val * val_right) % 1000000007

class Solution:
    def invert(self, string):
        new_string = ''
        for ele in string:
            if ele == "0":
                new_string += '1'
            else:
                new_string += "0"
        
        return new_string
    
    def helper(self, n):   # O(n^2)
        if n == 1:
            return '0'
        prev = self.helper(n - 1)
        return prev + '1' + (self.invert(prev)[::-1])

    def findKthBit(self, n: int, k: int) -> str:
        n_bit = self.helper(n)

        return n_bit[k - 1]

        
        
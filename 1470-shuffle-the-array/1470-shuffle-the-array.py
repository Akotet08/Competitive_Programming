class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        cp = [0] * 2*n
        for i in range(n):
            pos = i*2
            cp[pos] = nums[i]
            cp[pos+1] = nums[i+n]
        return cp
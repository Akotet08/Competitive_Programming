class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        count = 0
        prod = 1

        while i < len(nums):
            prod *= nums[i]
            while j <= i and prod >= k:
                prod /= nums[j]
                j += 1
            
            count += i -j +1
            i += 1

        return count

        
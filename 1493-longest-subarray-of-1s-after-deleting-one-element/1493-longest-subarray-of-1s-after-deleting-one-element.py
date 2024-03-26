class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        j = 0
        zero_count = 0
        one_count = 0

        while i < len(nums):
            if nums[i] == 0:
                zero_count += 1
            while j <= i and zero_count > 1:
                if nums[j] == 0:
                    zero_count -= 1
                j += 1
            
            one_count = max(one_count, i -j)
            i += 1
        return one_count
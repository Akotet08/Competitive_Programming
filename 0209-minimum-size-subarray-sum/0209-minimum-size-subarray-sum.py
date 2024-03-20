class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j = 0
        s = 0
        r = float('inf')

        for i in range(len(nums)):
            s += nums[i]
            while s >= target:
                r = min(r, i - j + 1)
                s -= nums[j]
                j += 1

        return 0 if r == float('inf') else r
        # return r

            

        
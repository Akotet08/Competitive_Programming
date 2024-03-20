class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        s = 0
        r = math.inf

        for i in range(len(nums)):
            s += nums[i]
            while s >= target:
                r = min(r, i - j + 1)
                s -= nums[j]
                j += 1

        if r == math.inf: return 0
        return r

            

        
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = max(nums)
        sett = set(nums)

        i = 0
        while i < m:
            if not i in sett:
                return i
            i += 1
        return m+1

        
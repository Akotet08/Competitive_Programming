class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        forward_sum = 0
        total = sum(nums)

        for i in range(n):
            if (forward_sum) == total-(forward_sum + nums[i]):
                return i
            forward_sum += nums[i]
        return -1
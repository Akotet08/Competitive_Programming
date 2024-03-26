class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        forward_sum = [0] * (n)
        forward_sum[0] = nums[0]

        total = sum(nums)

        for i in range(1, n):
            forward_sum[i] = forward_sum[i-1] + nums[i]
        
        for i in range(n):
            if (forward_sum[i] - nums[i]) == total-(forward_sum[i]):
                return i
        return -1
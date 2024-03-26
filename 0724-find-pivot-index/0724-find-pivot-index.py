class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        forward_sum = [0] * (n)
        forward_sum[0] = nums[0]

        back_sum = [0] * (n)
        back_sum[-1] = nums[-1]

        for i in range(1, n):
            forward_sum[i] = forward_sum[i-1] + nums[i]
        
        for j in range(n-2, -1, -1):
            back_sum[j] = back_sum[j + 1] + nums[j]
        
        for i in range(n):
            if forward_sum[i] == back_sum[i]:
                return i
        return -1
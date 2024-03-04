class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        mx = nums[0] + nums[-1]
        for i in range(1, len(nums)//2):
           s = nums[i] + nums[len(nums) - i - 1]
           if s > mx:
               mx = s
        return mx
        
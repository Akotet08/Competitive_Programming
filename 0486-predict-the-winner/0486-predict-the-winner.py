class Solution:
    def helper(self, nums, i, j):
        if i == j:
            return nums[i]
        
        left = nums[i] - self.helper(nums, i + 1, j)
        right = nums[j] - self.helper(nums, i, j-1)
        
        return max(left, right) 

    def predictTheWinner(self, nums: List[int]) -> bool:
        return (self.helper(nums, 0, len(nums) - 1) >= 0)

        
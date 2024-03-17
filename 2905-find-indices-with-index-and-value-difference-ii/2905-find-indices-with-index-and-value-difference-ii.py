class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        i = indexDifference
        ind = indexDifference
        min_idx = 0
        max_idx = 0

        while i < len(nums):
            if nums[i - ind] <= nums[min_idx]: min_idx = i - ind
            elif nums[i - ind] >= nums[max_idx]: max_idx = i - ind
            
            if(nums[i] - nums[min_idx] >= valueDifference): return[min_idx, i]
            elif(nums[max_idx] - nums[i] >= valueDifference): return [max_idx, i]
            i += 1
        return [-1, -1]
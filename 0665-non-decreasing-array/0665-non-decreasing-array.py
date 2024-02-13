class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        missplaced = 0
        changed = 0
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i+1]:
                continue
            
            if i == 0 or nums[i+1] >= nums[i-1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]

            changed += 1
        return changed <= 1
        


            
            
        return missplaced <= 1
        
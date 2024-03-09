class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 1
        seeker = 1
        count = 1

        while seeker < len(nums):
            if nums[seeker - 1] == nums[seeker]:
                count += 1
            else:
                count = 1
                
            if count > 2:
                while seeker < len(nums) and nums[seeker - 1] == nums[seeker]:
                    seeker += 1
            else:
                nums[pos] = nums[seeker]
                pos += 1
                seeker += 1
        
        return pos
                
                

            
                

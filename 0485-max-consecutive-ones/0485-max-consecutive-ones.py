class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        mx = nums[0]
        while i < len(nums):
            j = i + 1
            if nums[i] == 1:
                while j < len(nums) and  nums[j] == 1:
                    j += 1
                
                if j - i + 1 > mx:
                    mx = j - i

            i = j
        return mx 
                

        
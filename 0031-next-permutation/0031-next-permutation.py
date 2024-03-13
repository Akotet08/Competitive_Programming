class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        j = i-1
        while j>=0 and nums[j] >= nums[i]:
            j -= 1
            i -= 1
        
        if j < 0:
            nums.sort()
        else:
            n = len(nums)-1 
            while n >= 0 and nums[n] <= nums[j]:
                n -= 1
            nums[n], nums[j] = nums[j], nums[n]

            k = j + 1
            r = len(nums) - 1
            while k < r:
                nums[k], nums[r] = nums[r], nums[k]
                k += 1
                r -= 1
            
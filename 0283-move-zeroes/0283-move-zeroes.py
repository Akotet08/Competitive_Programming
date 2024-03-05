class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seeker = 0
        zero = 0

        while seeker < len(nums):
            if nums[zero] == 0:
                while seeker < len(nums) and nums[seeker] == 0:
                    seeker += 1
                if seeker < len(nums):
                    nums[zero], nums[seeker] = nums[seeker], nums[zero]
                zero += 1
                seeker = zero
            else:
                zero+=1
                seeker+=1
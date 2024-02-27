class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = [0,0,0]
        for ele in nums:
            size[ele] += 1
        
        idx = 0
        for i in range(3):
            for j in range(size[i]):
                nums[j + idx] = i
            idx += size[i]     

        
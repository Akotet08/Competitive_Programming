class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        lst = [nums[-i] for i in range(1, k+1)]

        if k == 0:
            return

        j = len(nums) - k -1
        i = len(nums) - 1
        while j >= 0 and i > j:
            nums[i], nums[j] = nums[j], nums[i]
            i -= 1
            j -= 1
        
        for i in range(k):
            nums[i] = lst[k-1-i]
        print(nums)
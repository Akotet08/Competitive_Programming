class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse = True)
        for i in range(n - 2):
            a = nums[i]
            b = nums[i+1]
            c = nums[i+2]

            if a + b > c and b+c > a and c+a > b:
                return a+b+c
        
        return 0

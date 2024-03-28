class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forward = [1] * (n + 1)
        backward = [1] * (n + 1)

        for i in range(n):
            forward[i + 1] = forward[i] * nums[i]
        for j in range(n-1, -1, -1):
            backward[j] = backward[j + 1] * nums[j]
        
        lst = [1] * n

        for i in range(n):
            lst[i] = backward[i+1] * forward[i]

        return lst

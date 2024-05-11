class Solution:
    def binary(self, array, target, r, l):
        r = r
        l = l
        while l <= r:
            mid = (l+r) // 2
            if array[mid] < target:
                l = mid + 1 
            else:
                r = mid - 1
        
        return l

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.binary(nums, target, len(nums) - 1, 0)
        second = self.binary(nums, target + 1, len(nums) - 1, first) - 1

        if first < len(nums) and nums[first] == target:
            return [first, second]
        
        return [-1, -1]
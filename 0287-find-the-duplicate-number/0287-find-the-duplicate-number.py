class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tort = nums[0]
        hare = nums[nums[0]]

        while hare != tort:
            hare = nums[nums[hare]]
            tort = nums[tort]
        
        tort = 0
        while tort != hare:
            tort = nums[tort]
            hare = nums[hare]

        return hare
        
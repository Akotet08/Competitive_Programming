class Solution:
    def back(self, nums, idx,  current, subsets):
        subsets.append(current[:])     

        for i in range(idx, len(nums)):
            current.append(nums[i])
            self.back(nums, i + 1, current, subsets)
            current.pop() # backtrack

    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        self.back(nums, 0, [], subsets)
        return subsets
                
                
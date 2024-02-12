class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = {nums[i]:i for i in range(len(nums))}

        for oper in operations:
            f, s = oper
            i = dic[f]

            dic[s] = i
            nums[i] = s
        
        return nums

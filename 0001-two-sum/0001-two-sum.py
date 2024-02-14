class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {nums[i] : i for i in range(len(nums))}

        for j, ele in enumerate(nums):
            second_num =  target - ele
            if second_num in dic and j != dic[second_num]:
                return [dic[second_num], j]


        
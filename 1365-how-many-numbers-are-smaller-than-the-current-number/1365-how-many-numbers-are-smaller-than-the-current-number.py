class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic = {}
        for i, ele in enumerate(nums):
            if ele in dic:
                dic[ele].append(i)
            else:
                dic[ele] = [i]
        
        nums.sort()
        lst = [0] * len(nums)
        i = 0
        while i < len(nums):
            if nums[i] in dic:
                idxes = dic[nums[i]]
                for idx in idxes:
                    lst[idx] = i
                
                del dic[nums[i]]
            i+=1
        return lst
            
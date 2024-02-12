class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        for ele in nums:
            if ele in dic:
                dic[ele] += 1
            else:
                dic[ele] = 1
        
        lst = []
        for ele in dic:
            if dic[ele] > (len(nums) // 3 ):
                lst.append(ele)
        
        return lst
        
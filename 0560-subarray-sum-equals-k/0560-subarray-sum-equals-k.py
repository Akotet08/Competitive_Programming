class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sum_set = {}
        count = 0
        ele = 0
        for i in nums:
            ele += i
            if ele == k:
                count += 1
            
            count += sum_set.get(ele-k, 0)
            sum_set[ele] = sum_set.get(ele, 0) + 1
        
        return count

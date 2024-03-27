class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sum_set = Counter()
        count = 0
        ele = 0
        for i in nums:
            ele += i
            if ele == k:
                count += 1
            if ele - k in sum_set:
                count += sum_set[ele-k]
            
            sum_set[ele] += 1
        
        return count

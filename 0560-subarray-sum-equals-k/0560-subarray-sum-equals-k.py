class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = [0] * (len(nums))
        prefix_sum[0] = nums[0]

        for idx in range(1, len(nums)):
            prefix_sum[idx] = prefix_sum[idx-1] + nums[idx]
        
        sum_set = Counter()
        count = 0
        for ele in prefix_sum:
            if ele == k:
                count += 1
            if ele - k in sum_set:
                count += sum_set[ele-k]
            
            sum_set[ele] += 1
        
        return count

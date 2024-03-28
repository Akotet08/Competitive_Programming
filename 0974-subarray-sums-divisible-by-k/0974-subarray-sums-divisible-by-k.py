class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        seen = Counter()
        seen[0] = 1
        prfx = 0
        count = 0

        for num in nums:
            prfx += num
            count += seen[prfx % k]
            seen[prfx % k] += 1
        
        return count

        
        
        return 0
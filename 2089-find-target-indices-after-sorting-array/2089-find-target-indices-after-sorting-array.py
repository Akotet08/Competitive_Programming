class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        pos = 0
        count = 0

        for ele in nums:
            if ele < target:
                pos += 1
            elif ele == target:
                count += 1
        
        lst = list(range(pos, pos+count))
        return lst
        
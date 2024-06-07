class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def back(nums, idx, current, k, res):
            if len(current) == k:
                res.append(current[:])
                return
            
            for i in range(idx, len(nums)):
                current.append(nums[i])
                back(nums, i +1, current, k, res)
                current.pop()
        
        nums = [i+1 for i in range(n)]
        res = []
        back(nums, 0, [], k, res)

        return res
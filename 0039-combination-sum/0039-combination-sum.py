class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def back(cand, idx, current, target, res):
            if sum(current) == target:
                res.append(current[:])
                return
            elif sum(current) > target:
                return
            
            for i in range(idx, len(cand)):
                current.append(cand[i])
                back(cand, i, current, target, res)
                current.pop()
        
        res = []
        back(candidates, 0, [], target, res)
        return res







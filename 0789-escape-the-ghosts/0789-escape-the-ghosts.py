class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        tx, ty = target

        clst_ghost = float('inf')
        for ghost in ghosts:
            gx, gy = ghost

            dis = abs(tx-gx) + abs(ty-gy)

            if dis <  clst_ghost:
                clst_ghost = dis
        
        d = abs(tx) + abs(ty)
        return clst_ghost > d
   
        
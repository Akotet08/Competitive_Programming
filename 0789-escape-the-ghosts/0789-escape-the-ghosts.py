class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        tx, ty = target

        clst_ghost = float('inf')
        for ghost in ghosts:
            gx, gy = ghost

            dis = sum([abs(tx-gx), abs(ty-gy)])

            if dis <  clst_ghost:
                clst_ghost = dis
        
        d = abs(tx) + abs(ty)

        print(clst_ghost, d)

        return clst_ghost > d
   
        
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        dic = {}
        for i in range(len(fronts)):
            f = fronts[i]
            b = backs[i]
            if f in dic:
                dic[f].add(b)
                if not b in dic:
                    dic[b] = {f}
            else:
                if not b in dic:
                    dic[b] = {f}
                dic[f] = {b}

        for i in range(1, 2001):
            if i in dic and not i in dic[i]:
                return i
        return 0



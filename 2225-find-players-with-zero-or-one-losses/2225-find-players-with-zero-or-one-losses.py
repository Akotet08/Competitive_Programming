class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic = {}
        for ele in matches:
            winner, loser = ele
            if loser in dic:
                dic[loser] += 1
            if not winner in dic:
                dic[winner] = 0
            if not loser in dic:
                dic[loser] = 1

        lst = [[], []]
        for ele in dic:
            if dic[ele] == 0:
                lst[0].append(ele)
            elif dic[ele] == 1:
                lst[1].append(ele)

        lst[0].sort()
        lst[1].sort()
        return lst


        
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        lst = [(names[i], heights[i]) for i in range(len(names))]
        lst.sort(reverse=True, key=lambda x: x[1])

        names = [ele[0] for ele in lst]
        return names
        
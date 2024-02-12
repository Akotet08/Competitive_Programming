class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = { list1[i]: i for i in range(len(list1))}

        min_val = len(list1) + len(list2)
        strs = {}

        for j, string in enumerate(list2):
            if string in dic and dic[string] + j <= min_val:
                min_val = dic[string] + j
                if min_val in strs:
                    strs[min_val].append(string)
                else:
                    strs[min_val] = [string]

        return strs[min(list(strs.keys()))]
        




        
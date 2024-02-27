class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {}
        for ele in arr1:
            if ele in dic:
                dic[ele] += 1
            else:
                dic[ele] = 1
        
        new_lst = []
        for ele in arr2:
            c = dic[ele]
            for _ in range(c):
                new_lst.append(ele)
            dic[ele] = 0
        
        add_list = []
        for key in dic:
            for _ in range(dic[key]):
                add_list.append(key)
        
        add_list.sort()
        return new_lst + add_list
        
        return new_lst
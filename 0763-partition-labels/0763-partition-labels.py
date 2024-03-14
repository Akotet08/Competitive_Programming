class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}

        for i, char in enumerate(s):
            if char in dic:
                dic[char][1] = i
            else:
                dic[char] = [i, i] 

        print(dic)
        partitions = []
        cur_start, cur_end = list(dic.values())[0]
        for start, end in dic.values():
            if start <= cur_end:
                cur_end = max(cur_end, end)
            else: # new partion
                partitions.append(cur_end - cur_start + 1)
                cur_start, cur_end = start, end
        partitions.append(cur_end - cur_start + 1)
        return partitions   
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for i in range(len(strs[0])):
            ps_prefix = strs[0][i]
            for j in strs:
                if i >= len(j): return prefix
                if j[i] != ps_prefix:
                    return prefix
            prefix += ps_prefix
        
        return prefix



        
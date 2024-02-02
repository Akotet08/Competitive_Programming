class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        comb = ''
        i, j = 0,0
        while i < len(word1) and j < len(word2):
            comb += word1[i]
            comb += word2[j]

            i+=1
            j+=1
        
        while(i < len(word1)):
            comb+=word1[i]
            i+=1
        while(j < len(word2)):
            comb+=word2[j]
            j+=1
        
        return comb
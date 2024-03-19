class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        i = 0
        j = 0
        length = 0
        while i < len(s):
            while s[i] in seen:
                seen.remove(s[j])
                j += 1
            
            seen.add(s[i])
            length = max(length, i -j + 1)

            i+=1
        return length
            

            
        
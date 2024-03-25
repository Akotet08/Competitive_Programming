class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        chars = set()
        prev = ''
        i = 0
        j = 0
        r = 0
        while i < len(word):
            chars.add(word[i])
            if prev != '' and word[i] < prev:
                while i < len(word) and word[i] != 'a':
                    i += 1
                chars = set()
                prev = ''
                j = i
                continue
            if len(chars) == 5:
                r = max(r, i -j +1)
            
            prev = word[i]
            i += 1
        return r



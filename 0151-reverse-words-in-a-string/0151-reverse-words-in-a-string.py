class Solution:
    def reverseWords(self, s: str) -> str:
        words = ''
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        
        while i < len(s):
            j = i+1
            while j < len(s) and s[j] != ' ': 
                j += 1
            
            words = s[i:j] + ' ' + words

            i = j
            while i < len(s) and s[i] == ' ':
                i+=1

        return words.strip()
            


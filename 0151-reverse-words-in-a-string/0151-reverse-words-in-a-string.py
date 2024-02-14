class Solution:
    def reverseWords(self, s: str) -> str:
        lst = []
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        
        while i < len(s):
            j = i+1
            while j < len(s) and s[j] != ' ': 
                j += 1
            
            lst.insert(0, s[i: j])

            i = j
            while i < len(s) and s[i] == ' ':
                i+=1

        return ' '.join(lst)
            


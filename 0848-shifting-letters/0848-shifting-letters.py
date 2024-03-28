class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(shifts)
        for i in range(n-2, -1, -1):
            shifts[i] += shifts[i+1]
        
        string = ''
        for i, shift in enumerate(shifts):
            val = ord(s[i]) + (shift % 26)
            if val > 122:
                val = ord('a') + ((val % 123) % 26)
            
            string +=chr(val)
        return string
        
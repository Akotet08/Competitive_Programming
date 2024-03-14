class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.checkhelper(a, b) or self.checkhelper(b, a)

    def checkhelper(self, a: str, b:str):
        i = 0
        j = len(a) - 1

        while i < j:
            if a[i]!=b[j]:
                break
            i += 1
            j -= 1
        
        temp_i = i
        temp_j = j
        while i < j:
            if a[i]!=a[j]:
                break
            i += 1
            j -= 1
        
        while temp_i < temp_j:
            if b[temp_i]!=b[temp_j]:
                break
            temp_i += 1
            temp_j -= 1
        
        return i >= j or (temp_i >= temp_j)

      
class Solution:
    def smallestNumber(self, num: int) -> int:
        n = list(str(num))

        if num < 0:
            n = n[1:]
            n.sort(reverse=True)
            return int('-' + ''.join(n))
        n.sort()
        
        for j in n:
            i = 0
            while i < len(n)-1 and n[i] == '0' :
                i+=1
            n[0], n[i] = n[i], n[0]


    
        return int(''.join(n))
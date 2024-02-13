class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        dic = {}
        
        for ele in A:
            if ele in dic:
                dic[ele] += 1
            else:
                dic[ele] = 1
        
        for ele in B:
            if not ele in dic:
                return False
            else:
                dic[ele] -= 1
        
        for ele in dic:
            if dic[ele] != 0:
                return False
        
        return True
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
       
        mid = len(skill) //2 
        i = 0
        prev_sum = skill[0] + skill[-1]
        chemistry = 0
        while i < mid:
            s = skill[i] + skill[len(skill) - i -1]
            if s == prev_sum:
                chemistry += skill[i] * skill[len(skill) - i -1]
            else:
                return -1
            
            i += 1
        
        return chemistry
        


        
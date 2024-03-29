class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        i = 0
        j = len(people) - 1

        while i < j:
            if people[i] + people[j] > limit:
                j -= 1
            else:
                i += 1
                j -= 1

            boats += 1
             
        if i == j:
            boats += 1

        return boats
            
            
        
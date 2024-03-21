class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = Counter()

        i = 0
        j = 0
        count = 0
        while i < len(fruits):
            baskets[fruits[i]] += 1
            while len(baskets) > 2 and baskets[fruits[j]] > 0:
                baskets[fruits[j]] -= 1

                if baskets[fruits[j]] == 0: del baskets[fruits[j]]
                j += 1
            
            print(baskets)
            count = max(count, i-j+1)
            i += 1
        return count
                
        
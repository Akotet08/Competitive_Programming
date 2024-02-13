class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx_candies = 0

        for candy in candies:
            if candy > mx_candies:
                mx_candies = candy
        
        res = [False] * len(candies) 
        for idx, candy in enumerate(candies):
            if candy + extraCandies >= mx_candies:
                res[idx] = True
        
        return res

        
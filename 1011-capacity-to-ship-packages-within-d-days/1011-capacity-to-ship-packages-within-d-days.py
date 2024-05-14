class Solution:
    def isPossible(self, predicted_weight, days, weights):
        count = 1
        cur_sum = 0
        i = 0
        while i < len(weights):
            if cur_sum + weights[i] > predicted_weight:
                cur_sum = 0
                count += 1
            cur_sum += weights[i]
            i += 1
        
        print(predicted_weight, count <= days)
        return count <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_weight = max(weights)
        max_weight = sum(weights)
        
        while min_weight < max_weight:
            mid = (min_weight + max_weight) // 2
            
            if self.isPossible(mid, days, weights):
                max_weight = mid
            else:
                min_weight = mid + 1
        
        return min_weight

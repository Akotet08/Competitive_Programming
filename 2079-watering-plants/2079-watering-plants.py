class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        curr_cap = capacity
        for idx, amount in enumerate(plants):
            if amount <= curr_cap:
                curr_cap -= amount
                steps += 1
            else:
                steps += 2*(idx) + 1
                curr_cap = capacity

                curr_cap -= amount
        return steps
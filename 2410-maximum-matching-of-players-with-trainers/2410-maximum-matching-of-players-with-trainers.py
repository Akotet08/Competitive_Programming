class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)

        i = 0
        j = 0
        count = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                i += 1
                j += 1
                count += 1
            else:
                i += 1
        
        return count

        
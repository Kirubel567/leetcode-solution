class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        player, trainer, count = 0, 0, 0

        players.sort()
        trainers.sort()

        while player < len(players) and trainer < len(trainers): 
            if players[player] <= trainers[trainer]: 
                count += 1
                trainer += 1
                player += 1
            else: 
                trainer += 1

        return count 
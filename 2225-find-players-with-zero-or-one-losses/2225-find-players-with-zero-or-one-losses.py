class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = []
        winners = []
        mapp = defaultdict(int)

        for i in range(len(matches)): 
            winners.append(matches[i][0])
            losers.append(matches[i][1])
            mapp[matches[i][1]]+=1
    

        losersSet = set(losers)
        onlyWinners= []
        for i in range(len(winners)): 
            if winners[i] not in losersSet and winners[i] not in onlyWinners: 
                onlyWinners.append(winners[i])
        onlyLosers = []
        for i in range(len(losers)): 
            if mapp[losers[i]] == 1: 
                onlyLosers.append(losers[i])

        return [sorted(onlyWinners), sorted(onlyLosers)]
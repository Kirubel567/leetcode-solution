class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        count = defaultdict(int)
        ans = float('inf')
        for i, value in enumerate(cards): 
            if cards[i] not in count: 
                count[cards[i]] = i
            else: 
                ans = min(ans, i - count[cards[i]] +1)
                count[cards[i]] = i
                
        return ans if ans != float('inf') else -1
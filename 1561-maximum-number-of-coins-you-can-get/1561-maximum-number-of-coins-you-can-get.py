class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        #use two pointer technique after sorting the array 
        piles.sort()
        smallest, middle = 0, len(piles)-2
        ans = 0
        while smallest < middle: 
            ans += piles[middle]
            smallest += 1
            middle -= 2
        return ans 
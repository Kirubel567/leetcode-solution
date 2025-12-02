class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = prices[::]
        stk = []
        for i in range(len(prices)-1, -1, -1): 
            while stk and stk[-1] > prices[i]: 
                stk.pop()
            if stk: 
                ans[i] = prices[i] - stk[-1]

            stk.append(prices[i])
        
        return ans
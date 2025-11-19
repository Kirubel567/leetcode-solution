class Solution:
    def maxCoins(self, piles):
        piles.sort()
        n = len(piles)
        
        left = 0                
        right = n - 1        
        answer = 0
        
        
        for _ in range(n // 3):
            right -= 1          
            answer += piles[right]  
            right -= 1          
            left += 1            
        
        return answer

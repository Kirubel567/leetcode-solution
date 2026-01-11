class Solution:
    def countBits(self, n: int) -> List[int]:
        def to_binary(n): 
            count = 0 
            while n > 0: 
                if n%2 == 1: 
                    count += 1
                n //= 2
            
            return count
        
        ans = []
        for i in range(n+1): 
            ans.append(to_binary(i))
        return ans 
            


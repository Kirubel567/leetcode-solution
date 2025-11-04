class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited: 
            visited.add(n)

            Sum = 0
            while n > 0: 
                digit = n % 10
                Sum += digit ** 2
                n = n //10
            n = Sum 

            if n == 1: 
                return True

        return False
        
        
            
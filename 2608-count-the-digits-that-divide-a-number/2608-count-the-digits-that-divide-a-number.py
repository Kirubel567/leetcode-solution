class Solution:
    def countDigits(self, num: int) -> int:
        
        
        n = num 
        count = 0
        while n > 0: 
            digit = n % 10
            if num % digit == 0: 
                count = count + 1
            n = n // 10
        return count 
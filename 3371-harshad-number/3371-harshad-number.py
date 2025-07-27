class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        y = x
        sum = 0
        while(y > 0): 
            digit = y % 10
            sum += digit 
            y //= 10
        
        return sum if (x%sum) == 0 else -1
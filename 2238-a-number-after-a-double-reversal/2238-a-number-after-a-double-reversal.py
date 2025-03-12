class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        Num = num
        reversed1 = 0
        while num > 0:
            digit = num % 10
            reversed1 = reversed1 * 10 + digit
            num //= 10
        reversed2 = 0
        while reversed1 > 0:
            digit1 = reversed1 % 10
            reversed2 = reversed2 * 10 + digit1
            reversed1 //= 10
        
        return reversed2 == Num
           
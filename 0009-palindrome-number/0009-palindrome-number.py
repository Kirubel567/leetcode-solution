class Solution:
    def isPalindrome(self, x: int) -> bool:
        #get the last digit until x is zero
        #build the reversed number while getting the last digit using the modulo 
        if x < 0: 
            return False
        
        reversed = 0
        compare = x 
        while compare > 0: 
            lastDigit = compare % 10
            reversed = reversed * 10 + lastDigit
            compare //=10

        return reversed == x

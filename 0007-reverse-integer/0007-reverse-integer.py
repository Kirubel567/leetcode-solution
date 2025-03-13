class Solution:
    def reverse(self, x: int) -> int:
        num = 0 
        if x >= 0:
            while x > 0:
                digit = x % 10 
                num = num * 10 + digit 
                x //= 10 
        elif x < 0:
            num = int(str(x * -1)[::-1]) * -1
        if num > 2 ** 31 - 1 or num < -2 ** 31:
            return 0   

        return num   

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))

        while left <= right: 
            Sum = left**2 + right**2

            if Sum == c: 
                return True 
            elif Sum < c: 
                left += 1
            else: 
                right -=1

        return False
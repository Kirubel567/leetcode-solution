class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        string = str(x)
        print(string[::-1])
        return int(string[::-1]) == x
    
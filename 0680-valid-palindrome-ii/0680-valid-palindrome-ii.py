class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r: 
            if s[l] != s[r]: 
                lRemoved, rRemoved = s[l+1: r+1], s[l:r]
                return (lRemoved == lRemoved[::-1] or rRemoved == rRemoved[::-1])
            l+=1
            r-=1
        return True 
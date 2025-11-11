class Solution:
    def freqAlphabets(self, s: str) -> str:
        # a = 65, but a is 65 -96 that's 1, so you can simply deduct 96 from each characters to find their number
        #use the while loop to easily manipulate the iterating variable
        i = len(s)-1
        ans = ''
        while i >=0: 
            if s[i] != '#':
                ch = chr(int(s[i])+96)
                ans += ch
                i -=1
            else: 
                curr = ''
                curr = s[i-2:i]
                ch = chr(int(curr)+96)
                ans += ch
                i -= 3
        return ans[::-1] 



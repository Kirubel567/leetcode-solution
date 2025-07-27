class Solution:
    def replaceDigits(self, s: str) -> str:
        arr = []
        arr.append(s[0])
        for i in range(1, len(s)): 
            if s[i].isdigit(): 
                arr.append(chr(ord(s[i - 1]) + int(s[i])))
            else: 
                arr.append(s[i])
        return ''.join(arr)


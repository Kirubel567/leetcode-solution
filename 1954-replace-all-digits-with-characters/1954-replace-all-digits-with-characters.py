class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(ch, x):
            num = ord(ch) + x
            return chr(num)
        arr = []
        arr.append(s[0])
        for i in range(1, len(s)): 
            if s[i].isdigit(): 
                arr.append(shift(s[i - 1], int(s[i])))
            else: 
                arr.append(s[i])
        return ''.join(arr)


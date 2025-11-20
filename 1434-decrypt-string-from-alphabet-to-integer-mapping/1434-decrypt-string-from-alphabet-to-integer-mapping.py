class Solution:
    def freqAlphabets(self, s: str) -> str:
        #the character a is 97
        #adding 96 to all of the numbers give the character in question 
        #iterate through each number in the string, use while loop to better control the variables 
        i, toWord = 0, ""

        while i < len(s): 
            converted = ""
            if i < len(s) - 2 and s[i+2] == "#": 
                converted = s[i] + s[i+1]
                i += 2
            else: 
                converted = s[i]
            toWord += chr(int(converted)+96)
            i+=1
        return toWord
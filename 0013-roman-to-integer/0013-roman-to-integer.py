class Solution:
    def romanToInt(self, s: str) -> int:
        #use a hash table to do this quesiton 
        mapp = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D":500, "M": 1000}

        Sum = 0
        i = 0 
        while i < len(s):
            if s[i] == "I" and i != len(s) -1:
                if s[i + 1] == "V":   
                    Sum += 4
                    i += 2
                elif s[i + 1] == "X":
                    Sum += 9
                    i += 2
                else: 
                    Sum += mapp[s[i]]
                    i += 1

            elif s[i] == "X" and i != len(s) - 1:
                if s[i + 1] == "L":   
                    Sum += 40
                    i += 2
                elif s[i + 1] == "C":
                    Sum += 90
                    i += 2
                else: 
                    Sum += mapp[s[i]]
                    i += 1
            
            elif s[i] == "C" and i != len(s) - 1:
                if s[i + 1] == "D":   
                    Sum += 400
                    i += 2
                elif s[i + 1] == "M":
                    Sum += 900
                    i += 2
                else: 
                    Sum += mapp[s[i]]
                    i += 1
            else: 
                Sum += mapp[s[i]]
                i += 1
        
        return Sum 

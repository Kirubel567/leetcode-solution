class Solution:
    def isValid(self, s: str) -> bool:
        dict = {"(":")", "{":"}", "[":"]"}
        stk = []

        for i in range(len(s)): 
            if s[i] in dict.keys(): 
                stk.append(s[i])
            else: 
                if not stk: 
                    return False
                popped = stk.pop()
                if dict[popped] != s[i]: 
                    return False
        
        return stk == []
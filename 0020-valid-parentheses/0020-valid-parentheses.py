class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {"(":")", "{":"}", "[":"]"}
        stk = []

        for i in range(len(s)): 
            if s[i] in mapp.keys(): 
                stk.append(s[i])
            else: 
                if not stk: 
                    return False
                popped = stk.pop()
                if mapp[popped] != s[i]: 
                    return False
        
        return stk == []
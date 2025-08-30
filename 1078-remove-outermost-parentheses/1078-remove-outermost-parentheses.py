class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        output = ""
        
        for i in range(len(s)): 
            if s[i] == "(": 
                if len(stack) > 0: 
                    output += s[i]
                stack.append(s[i])
            else: 
                stack.pop()

                if len(stack) > 0: 
                    output += s[i]
        
        return output 

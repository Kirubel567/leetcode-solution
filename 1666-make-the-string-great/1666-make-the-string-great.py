class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) == 0: 
            return s
        
        stack = []

        for ch in s:
            if stack and abs(ord(ch) - ord(stack[-1])) == 32:
                stack.pop() 
            else: 
                stack.append(ch)

        return "".join(stack)
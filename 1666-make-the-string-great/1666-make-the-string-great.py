class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) == 0: 
            return s
        
        stack = []

        for ch in s:
            if stack and ch != stack[-1] and (ch == stack[-1].lower() or ch.lower() == stack[-1]):
                stack.pop() 
            else: 
                stack.append(ch)

        return "".join(stack)
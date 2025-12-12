class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        lastPointer = 0

        result = ""

        for idx in spaces:
            result += s[lastPointer: idx] + " "
            lastPointer = idx
        result += s[lastPointer:]
        
        return result 

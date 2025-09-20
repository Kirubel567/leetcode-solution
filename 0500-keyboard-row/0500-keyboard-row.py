class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        #another solution using sets only 
        firstRow = "qwertyuiop"
        secondRow = "asdfghjkl"
        thirdRow = "zxcvbnm"

        res = []
        for word in words: 
            if len(firstRow) == len(set(word.lower() + firstRow)) or len(secondRow) == len(set(word.lower() + secondRow)) or len(thirdRow) == len(set(word.lower() + thirdRow)): 
                res.append(word)

        return res 
            
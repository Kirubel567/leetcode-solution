class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        print(s)
        for ch in reversed(s):
            if ch != " " and ch!="": 
                return len(ch)
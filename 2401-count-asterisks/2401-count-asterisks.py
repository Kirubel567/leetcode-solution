class Solution:
    def countAsterisks(self, s: str) -> int:
        check = False
        count = 0

        for ch in s: 
            if ch == "|": 
                check = not check 
            elif not check and ch == "*": 
                count += 1

        return count 

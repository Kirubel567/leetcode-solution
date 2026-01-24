class Solution:
    def firstUniqChar(self, s: str) -> int:
        mapp = Counter(s)

        for i in range(len(s)): 
            if mapp[s[i]] == 1:
                return i
        
        return (-1)
        

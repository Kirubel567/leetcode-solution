class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)+1

        i, j = 0, len(s)
        ans = []
        for ch in s: 
            if ch == "I": 
                ans.append(i)
                i+=1
            else: 
                ans.append(j)
                j-=1
        ans.append(i)
        return ans 
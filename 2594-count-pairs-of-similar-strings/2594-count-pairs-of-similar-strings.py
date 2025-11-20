class Solution:
    def similarPairs(self, words: List[str]) -> int:
        hashableArr = [frozenset(word) for word in words]
        mapp = Counter(hashableArr)
        ans = 0
        for key in mapp: 
            if mapp[key] > 1: 
                ans += (mapp[key] * (mapp[key]-1))//2
        
        return ans 

        



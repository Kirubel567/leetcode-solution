class Solution:
    def similarPairs(self, words: List[str]) -> int:
        mapp = defaultdict(int)

        for i in range(len(words)): 
            key = ''.join(sorted(set(words[i])))
            mapp[key]+=1
        
        count = 0
        for key in mapp: 
            if mapp[key] >1:
                count += mapp[key] * (mapp[key] - 1) // 2
        return count 
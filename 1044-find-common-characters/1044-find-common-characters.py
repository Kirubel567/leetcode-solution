class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])

        for i in range(1, len(words)): 
            curr_cnt = Counter(words[i])
            for c in cnt: 
                cnt[c] = min(cnt[c], curr_cnt[c])
        
        res = []
        for key in cnt:
            for i in range(cnt[key]): 
                res.append(key)
        return res 
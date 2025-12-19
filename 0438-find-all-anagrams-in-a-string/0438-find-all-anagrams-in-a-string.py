class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = 0
        res = []
        pFreq = Counter(p)
        sCounter = Counter(s[l:len(p)])
        if pFreq == sCounter: 
            res.append(l)

        
        for r in range(len(p), len(s)): 
            sCounter[s[r]] += 1
            sCounter[s[l]] -= 1

            if sCounter[s[l]] == 0: 
                del sCounter[s[l]]
            
            l += 1
            if pFreq == sCounter: 
                res.append(l)
            

        return res
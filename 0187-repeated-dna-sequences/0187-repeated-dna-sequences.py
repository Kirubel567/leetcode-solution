class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mapp = defaultdict(int)
        res, seen = set(), set()

        for l in range(len(s)-9): 
            added = s[l:l+10]
            if added in seen: 
                res.add(added)
            seen.add(added)

        return list(res)



            





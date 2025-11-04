class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mapp = defaultdict(int)
        #use two maps one for storing the freq of the substr and one for the number of each characters in the substring 
        mapp[s[:10]] = 1
        left = 0
        for r in range(10, len(s)): 
            left += 1
            added = s[left:r+1]
            mapp[added] += 1


        print(mapp)
        res = []
        for key in mapp: 
            if mapp[key] > 1:
                res.append(key)
        
        
        return res

            





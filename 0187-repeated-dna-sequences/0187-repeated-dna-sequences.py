class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mapp = defaultdict(int)
        #use two maps one for storing the freq of the substr and one for the number of each characters in the substring 
        mapp[s[:10]] = 1
        left = 0
        res = []
        for r in range(10, len(s)): 
            left += 1
            added = s[left:r+1]
            if added in mapp and mapp[added] == 1: 
                res.append(added)
            mapp[added] += 1

       
        
        
        return res

            





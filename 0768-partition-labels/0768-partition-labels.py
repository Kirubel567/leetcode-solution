class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mapp = dict()
        for i, ch in enumerate(s): 
            mapp[ch] = i
        
        res = []
        size, ending = 0, 0
        for i, ch in enumerate(s): 
            size += 1
            ending = max(ending, mapp[ch])

            if i == ending:
                res.append(size) 
                size = 0
            
        return res

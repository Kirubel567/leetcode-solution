class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        max_idx, h_idx = 0, 0
        for i in range(len(citations)): 
            if len(citations)-i >= citations[i]: 
                max_idx = citations[i]
            else: 
                max_idx = len(citations)-i
            h_idx = max(max_idx, h_idx)
        return h_idx


        

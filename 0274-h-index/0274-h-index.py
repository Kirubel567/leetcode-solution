class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        max_idx, h_idx = 0, 0
        print(citations)
        for i in range(len(citations)): 
            h_idx = max(min(len(citations)-i, citations[i]), h_idx)
        return h_idx


        

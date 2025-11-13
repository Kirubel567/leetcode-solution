class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        length = 0

        for num in freq: 
            if num+1 in freq: 
                length = max(length, freq[num]+ freq[num+1])
        
        return length
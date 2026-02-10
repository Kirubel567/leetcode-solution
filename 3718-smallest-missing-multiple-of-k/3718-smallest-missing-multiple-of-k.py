class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        for i in range(k, 1000, k): 
            if i%k == 0 and i not in nums: 
                return i



class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = []

        for i in range(1, 2001):
            if i not in arr: 
                missing.append(i)

        for  i in range(len(missing)): 
            if i + 1 == k: 
                return missing[k-1]
        
        return 

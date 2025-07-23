class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int: 
        if arr[0] == 1 and len(arr) == 1: 
            return 2
        lst = [x for x in range(max(arr) * 100) if x not in arr]

        return lst[k % len(lst)]
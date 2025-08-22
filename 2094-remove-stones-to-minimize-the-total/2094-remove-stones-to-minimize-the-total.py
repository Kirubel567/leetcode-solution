class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        A = [-num for num in piles]
        heapq.heapify(A)
        for i in range(k): 
            heapq.heapreplace(A, A[0]//2)
        return -sum(A)
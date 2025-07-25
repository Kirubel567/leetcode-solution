class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        accumulate = 0
        prefix_sum = []
        for num in nums: 
            accumulate += num
            prefix_sum.append(accumulate)
        

        if prefix_sum[len(prefix_sum) - 1] - prefix_sum[0] == 0: 
            return 0
        for i in range(1, len(prefix_sum)): 
            if prefix_sum[i - 1] == prefix_sum[len(prefix_sum) - 1] - prefix_sum[i]: 
                return i

        return -1
   
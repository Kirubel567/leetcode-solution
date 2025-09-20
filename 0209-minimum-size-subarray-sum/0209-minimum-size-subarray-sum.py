class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        Sum, indexStart, length = 0, 0, float('inf')
        for i in range(len(nums)): 
            Sum += nums[i]

            while Sum >= target: 
                length = min(i - indexStart + 1, length)
                Sum -= nums[indexStart]
                indexStart += 1
        
        return 0 if length == float('inf') else length
                
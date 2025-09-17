class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        Sum, targetIdx, compare = 0, 0, float("inf")
        for i in range(len(nums)): 
            Sum += nums[i]
        
            while Sum >= target: 
                count = i - targetIdx + 1
                compare = min(compare, count)
                    
                Sum -= nums[targetIdx]
                targetIdx += 1
            
        
        return 0 if compare == float('inf') else compare
            
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: 
            return 0
        Sum, count, i, targetIdx, compare = 0, 0, 0, 0, float("inf")
        while i < len(nums): 
            Sum += nums[i]
        
            while Sum >= target: 
                count = i - targetIdx + 1
                if count < compare: 
                    compare = count 
                Sum -= nums[targetIdx]
                targetIdx += 1
                
            
            i += 1
        
        return compare
            
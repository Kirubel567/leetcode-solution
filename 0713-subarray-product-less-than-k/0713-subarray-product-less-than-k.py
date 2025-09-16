class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: 
            return 0 

        indexTracker, Product, count = 0, 1, 0

        for i in range(len(nums)): 
            Product *= nums[i]
            
            while Product >= k: 
                Product //= nums[indexTracker]
                indexTracker += 1
            
            count += i - indexTracker + 1
            
        return count 

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        Sum, count = 0, 0
        for i in range(len(nums)): 
            if nums[i] < 0: 
                Sum -= -(nums[i])
    
            elif nums[i] > 0: 
                Sum += nums[i]
            
            if Sum == 0: 
                count += 1

        return count
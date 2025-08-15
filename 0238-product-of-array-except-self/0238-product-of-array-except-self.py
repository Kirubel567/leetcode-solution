class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) 

        #prefix 
        accumulator = 1
        for i in range(len(nums)): 
            res[i] *= accumulator 
            accumulator *= nums[i]
            
        #postfix
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= prod 
            prod *= nums[i] 
            

        return res
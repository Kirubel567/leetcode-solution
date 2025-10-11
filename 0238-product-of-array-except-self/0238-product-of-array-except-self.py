class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref_sum, post_sum = 1, 1 
        res = [1]*len(nums)

        for i in range(len(nums)): 
            res[i] *= pref_sum
            pref_sum *= nums[i]
        
        for i in range(len(nums)-1, -1, -1): 
            res[i] *= post_sum
            post_sum *= nums[i]

        return res 
